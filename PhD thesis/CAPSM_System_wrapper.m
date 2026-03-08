%% CAPSM_System_wrapper.m
% MATLAB wrapper for CAPSM S-function

function y = CAPSM_System_wrapper(u, S1, S2, net, cfg)
%CAPSM_SYSTEM_WRAPPER  Calls compiled CAPSM S-function
%
%  y = CAPSM_System_wrapper(u, S1, S2, net, cfg)
%
% INPUTS:
%   u [N_bus*2+1, 1]   - Grid observations (V_mag, V_ang, freq)
%   S1 [struct]         - System-1 (CNN-LSTM) parameters
%   S2 [struct]         - System-2 (QIRL) parameters
%   net [struct]        - Network data
%   cfg [struct]        - Configuration
%
% OUTPUTS:
%   y [20, 1]  - Control commands [P_setpoint; Q_support]

persistent S1_cached S2_cached

if nargin == 0 || isempty(u), y = zeros(20, 1); return; end

if isempty(S1_cached)
    S1_cached = S1;
    S2_cached = S2;
end

try
    % Parse observations
    V_mag = u(1:39);
    V_ang = u(39+1:78);
    freq = u(end);

    % System-1: Fast reflex
    [P_s1, Q_s1, conf_s1] = evaluate_system1(V_mag, V_ang, freq, S1_cached);

    % System-2: Deliberation
    [P_s2, Q_s2, Q_val] = evaluate_system2(V_mag, V_ang, freq, S2_cached);

    % Arbitration
    [P_final, Q_final] = arbitrate_actions(P_s1, Q_s1, conf_s1, P_s2, Q_s2, Q_val);

    y = [P_final; Q_final];

catch ME
    warning('CAPSM evaluation failed: %s', ME.message);
    y = zeros(20, 1);
end

end
