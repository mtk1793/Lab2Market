%% build_capsm_simulink_model.m
% Automated Simulink model generation for CAPSM
% Generated on 2026-03-05 11:33:05

clear all; close all; clc;

fprintf('CAPSM Simulink Model Builder\n');
fprintf('====================================\n\n');

% Check Simulink availability
if ~license('test', 'Simulink')
    fprintf('ERROR: Simulink license not available\n');
    return;
end

% Step 1: Load network data
fprintf('[1/5] Loading IEEE 39-bus network...\n');
net = load_ieee39_network_enhanced();

% Step 2: Configure system
fprintf('[2/5] Configuring CAPSM parameters...\n');
cfg = struct();
cfg.test_system = 'IEEE39';
cfg.T_sim = 600;           % 600 second simulation
cfg.dt = 0.001;             % 1 ms time step
cfg.dt_pf = 0.01;           % 10 ms power flow step
cfg.verbose = true;
cfg.use_gpu = false;

% Step 3: Create Simulink model
fprintf('[3/5] Building Simulink model...\n');
model = create_simulink_model(net, cfg);

% Step 4: Configure solver and diagnostics
fprintf('[4/5] Configuring solver...\n');
if isfield(model, 'created') && model.created
    try
        set_param(model.name, 'Solver', 'ode45');
        set_param(model.name, 'SolverType', 'Variable-step');
        set_param(model.name, 'AbsTol', '1e-4');
        set_param(model.name, 'RelTol', '1e-3');
        set_param(model.name, 'MaxStep', '0.01');
    catch
        fprintf('Could not configure all solver parameters\n');
    end
end

% Step 5: Save and display
fprintf('[5/5] Saving model...\n');
if isfield(model, 'name') && ~isempty(model.name)
    output_file = sprintf('CAPSM_Model_%s.slx', datestr(now, 'yymmdd'));
    try
        save_system(model.name, output_file);
        fprintf('\nModel saved to: %s\n', output_file);
        fprintf('Ready for simulation!\n\n');
    catch ME
        fprintf('Error saving model: %s\n', ME.message);
    end
else
    fprintf('Model creation was not successful\n');
    return;
end
