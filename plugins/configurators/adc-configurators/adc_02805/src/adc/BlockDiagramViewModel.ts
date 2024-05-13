import {
  useIntegerSymbol,
  useFloatSymbol,
  useBooleanSymbol,
  useKeyValueSetSymbol,
  useStringSymbol,
  PluginConfigContext,
  stringSymbolApi
} from '@mplab_harmony/harmony-plugin-client-lib';
import { createContext, useContext, useEffect, useState } from 'react';

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
  const operationMode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'AD1CON1__MODE12'
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
  const totalPins = useIntegerSymbol({
    componentId,
    symbolId: 'ADC_NUM_OF_PINS'
  });

  const [isVddCoreMaskVisible, setVddCoreMaskVisibility] = useState<boolean>(false);

  const [resultRegisters, setResultRegisters] = useState<string[]>([]);

  useEffect(() => {
    stringSymbolApi.getValue('core', 'PRODUCT_FAMILY').then(initializeState);
  }, []);

  function initializeState(productFamily: string) {
    if (productFamily === 'PIC32MM1387') {
      setVddCoreMaskVisibility(false);
      setResultRegisters(['ADC1BUF19', 'ADC1BUF20', 'ADC1BUF21']);
    } else {
      setVddCoreMaskVisibility(true);
      setResultRegisters(['ADC1BUF13', 'ADC1BUF14', 'ADC1BUF15']);
    }
  }

  return {
    clockDivider,
    clockSource,
    clockSourceInputFrequency,
    tad,
    voltageReference,
    outputFormat,
    resultBufferMode,
    enableAutoSampling,
    operationMode,
    autoSampleTime,
    conversionTriggerSource,
    interrupt,
    samplesPerInterrupt,
    stopInIdleMode,
    scanEnable,
    positiveInputA,
    totalPins,
    isVddCoreMaskVisible,
    resultRegisters
  };
};

export default useBlockDiagramViewModel;

export type BlockDiagramViewModel = ReturnType<typeof useBlockDiagramViewModel>;

export const BlockDiagramContext = createContext<BlockDiagramViewModel | null>(null);
