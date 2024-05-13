import {
  useIntegerSymbol,
  useFloatSymbol,
  useBooleanSymbol,
  useKeyValueSetSymbol,
  useStringSymbol,
  PluginConfigContext
} from '@mplab_harmony/harmony-plugin-client-lib';
import { createContext, useContext } from 'react';

const useBlockDiagramViewModel = () => {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const clockDivider = useIntegerSymbol({
    componentId,
    symbolId: 'AD1CON3__ADCS'
  });
  const clockSource = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON3__ADRC'
  });
  const clockSourceInputFrequency = useStringSymbol({
    componentId: 'core',
    symbolId: 'CONFIG_SYS_CLK_PBCLK_FREQ'
  });

  const tad = useFloatSymbol({ componentId, symbolId: 'ADC_TCLK' });
  const voltageReference = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON2__VCFG'
  });
  const outputFormat = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON1__FORM'
  });
  const resultBufferMode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON2__BUFM'
  });
  const enableAutoSampling = useBooleanSymbol({
    componentId,
    symbolId: 'AD1CON1__ASAM'
  });
  const stopAutoSamplingAfter1stConversionSequence = useBooleanSymbol({
    componentId,
    symbolId: 'AD1CON1__CLRASAM'
  });
  const autoSampleTime = useIntegerSymbol({
    componentId,
    symbolId: 'AD1CON3__SAMC'
  });
  const conversionTriggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON1__SSRC'
  });
  const interrupt = useBooleanSymbol({
    componentId,
    symbolId: 'ADC_INTERRUPT'
  });
  const samplesPerInterrupt = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON2__SMPI'
  });
  const stopInIdleMode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON1__SIDL'
  });
  const scanEnable = useBooleanSymbol({
    componentId,
    symbolId: 'AD1CON2__CSCNA'
  });
  const positiveInputA = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CHS__CH0SA'
  });
  const positiveInputB = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CHS__CH0SB'
  });
  const negativeInputA = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CHS__CH0NA'
  });
  const negativeInputB = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CHS__CH0NB'
  });
  const alternateInputSampleMode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON2__ALTS'
  });

  return {
    clockDivider,
    clockSource,
    clockSourceInputFrequency,
    tad,
    voltageReference,
    outputFormat,
    resultBufferMode,
    enableAutoSampling,
    stopAutoSamplingAfter1stConversionSequence,
    autoSampleTime,
    conversionTriggerSource,
    interrupt,
    samplesPerInterrupt,
    stopInIdleMode,
    scanEnable,
    positiveInputA,
    positiveInputB,
    negativeInputA,
    negativeInputB,
    alternateInputSampleMode
  };
};

export default useBlockDiagramViewModel;

export type BlockDiagramViewModel = ReturnType<typeof useBlockDiagramViewModel>;

export const BlockDiagramContext = createContext<BlockDiagramViewModel | null>(null);
