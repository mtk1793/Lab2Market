#define S_FUNCTION_NAME CAPSM_System
#define S_FUNCTION_LEVEL 2

#include "simstruc.h"
#include <math.h>
#include <string.h>

/* S-function parameters */
#define N_BUS 39
#define N_GEN 10
#define N_LINE 46
#define DT 0.001000

static void mdlInitializeSizes(SimStruct *S)
{
    ssSetNumSFcnParams(S, 0);
    if (ssGetNumSFcnParams(S) != ssGetSFcnParamsCount(S)) return;

    /* Input ports:
       0: Grid observations (V_mag, V_ang, freq)
       1: Control enabling signals
    */
    if (!ssSetNumInputPorts(S, 2)) return;
    ssSetInputPortWidth(S, 0, N_BUS*2+1);
    ssSetInputPortWidth(S, 1, 1);

    /* Output ports:
       0: Control actions (P_ref, Q_ref)
       1: System status
    */
    if (!ssSetNumOutputPorts(S, 2)) return;
    ssSetOutputPortWidth(S, 0, N_GEN);
    ssSetOutputPortWidth(S, 1, 1);

    /* Sample time */
    ssSetNumSampleTimes(S, 1);
    ssSetSimStateCompliance(S, USE_DEFAULT_SIM_STATE);
}

static void mdlInitializeSampleTimes(SimStruct *S)
{
    ssSetSampleTime(S, 0, DT);
    ssSetOffsetTime(S, 0, 0.0);
}

#define MDL_START
static void mdlStart(SimStruct *S) { }

static void mdlOutputs(SimStruct *S, int_T tid)
{
    InputRealPtrsType uPtrs = ssGetInputPortRealSignalPtrs(S, 0);
    real_T *y = ssGetOutputPortRealSignal(S, 0);
    int i;

    /* TODO: Call CAPSM control logic */
    for (i = 0; i < N_GEN; i++) {
        y[i] = (*uPtrs[0]) * 0.5;  /* Placeholder */
    }
}

static void mdlTerminate(SimStruct *S) { }
#include "simulink.c"
