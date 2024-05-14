import {
  useIntegerSymbol,
  useBooleanSymbol,
  useKeyValueSetSymbol,
  PluginConfigContext,
  useCommentSymbol,
  useComboSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { createContext, useContext, useEffect, useState } from 'react';

function getSuffixDigitsAsNumber(value: string) {
  if (value === undefined) {
    return 69696;
  }
  const matches = value.match(/(\d+)$/);
  if (matches) {
    return parseInt(matches[1], 10);
  }
  return 69696;
}

const useBlockDiagramViewModel = () => {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const salveEnable = useBooleanSymbol({ componentId, symbolId: 'ADC_CTRLA_SLAVEEN' });

  const startEventInput = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_EVCTRL_START' });
  const conversionTrigger = useComboSymbol({ componentId, symbolId: 'ADC_CONV_TRIGGER' });
  const flushEventInput = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_EVCTRL_FLUSH' });
  const enableUserSequenceMode = useBooleanSymbol({ componentId, symbolId: 'ADC_SEQ_ENABLE' });
  const enableRunInStandby = useBooleanSymbol({ componentId, symbolId: 'ADC_CTRLA_RUNSTDBY' });
  const enableOnDemandControl = useBooleanSymbol({ componentId, symbolId: 'ADC_CTRLA_ONDEMAND' });

  const prescaler = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_CTRLB_PRESCALER' });
  const [prescalerValue, setPrescalerValue] = useState(0);

  const resultResolution = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_CTRLC_RESSEL' });
  const positiveInputCombo = useKeyValueSetSymbol({
    componentId,
    symbolId: 'ADC_INPUTCTRL_MUXPOS'
  });
  const negativeInputCombo = useKeyValueSetSymbol({
    componentId,
    symbolId: 'ADC_INPUTCTRL_MUXNEG'
  });

  const accumulatedSampelsCombo = useKeyValueSetSymbol({
    componentId,
    symbolId: 'ADC_AVGCTRL_SAMPLENUM'
  });
  const rightShiftsNumbers = useIntegerSymbol({ componentId, symbolId: 'ADC_AVGCTRL_ADJRES' });
  const sampleLength = useIntegerSymbol({ componentId, symbolId: 'ADC_SAMPCTRL_SAMPLEN' });
  const referenceCombo = useKeyValueSetSymbol({
    componentId,
    symbolId: 'ADC_REFCTRL_REFSEL'
  });
  const convTime = useCommentSymbol({ componentId, symbolId: 'ADC_SAMPCTRL_SAMPLEN_TIME' });
  const [convTimeValue, setConvTimeValue] = useState('');

  const highThresholdSpinner = useIntegerSymbol({ componentId, symbolId: 'ADC_WINUT' });
  const lowThresholdSpinner = useIntegerSymbol({ componentId, symbolId: 'ADC_WINLT' });
  const comparsionModeCombo = useKeyValueSetSymbol({
    componentId,
    symbolId: 'ADC_CTRLC_WINMODE'
  });

  const enableWinmonInterrupt = useBooleanSymbol({ componentId, symbolId: 'ADC_INTENSET_WINMON' });
  const enableWinmonEvenOut = useBooleanSymbol({
    componentId,
    symbolId: 'ADC_WINDOW_OUTPUT_EVENT'
  });

  const enableleft_alignedResult = useBooleanSymbol({ componentId, symbolId: 'ADC_CTRLC_LEFTADJ' });
  const enableResultInterrupt = useBooleanSymbol({ componentId, symbolId: 'ADC_INTENSET_RESRDY' });
  const enableResultIEvent = useBooleanSymbol({ componentId, symbolId: 'ADC_EVCTRL_RESRDYEO' });

  useEffect(() => {
    const temp = convTime.label.replace('**** Conversion Time is ', '').replace(' ****', '');
    setConvTimeValue(temp);
  }, [convTime.label]);

  useEffect(() => {
    setPrescalerValue(getSuffixDigitsAsNumber(prescaler.selectedOption));
  }, [prescaler.selectedOption]);

  return {
    salveEnable,
    startEventInput,
    conversionTrigger,
    flushEventInput,
    enableUserSequenceMode,
    enableRunInStandby,
    enableOnDemandControl,
    prescaler,
    prescalerValue,
    resultResolution,
    positiveInputCombo,
    negativeInputCombo,
    accumulatedSampelsCombo,
    rightShiftsNumbers,
    sampleLength,
    referenceCombo,
    convTimeValue,
    highThresholdSpinner,
    lowThresholdSpinner,
    comparsionModeCombo,
    enableWinmonInterrupt,
    enableWinmonEvenOut,
    enableleft_alignedResult,
    enableResultInterrupt,
    enableResultIEvent
  };
};

export default useBlockDiagramViewModel;

export type BlockDiagramViewModel = ReturnType<typeof useBlockDiagramViewModel>;

export const BlockDiagramContext = createContext<BlockDiagramViewModel | null>(null);
