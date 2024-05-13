import {
  useIntegerSymbol,
  useBooleanSymbol,
  useKeyValueSetSymbol,
  PluginConfigContext,
  useCommentSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { createContext, useContext, useEffect, useState } from 'react';

const useBlockDiagramViewModel = () => {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const clockFreq = useIntegerSymbol({ componentId, symbolId: 'ADC_CLK' });
  const prescalar = useIntegerSymbol({ componentId, symbolId: 'ADC_MR_PRESCAL' });
  const clockSource = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_CLK_SRC' });

  const enableUserSequenceMode = useBooleanSymbol({ componentId, symbolId: 'ADC_MR_USEQ' });
  const triggerSelection = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_MR_TRGSEL_VALUE' });

  const conversionMode = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_CONV_MODE' });

  const convTime = useCommentSymbol({ componentId, symbolId: 'ADC_CONV_TIME' });
  const [convTimeValue, setConvTimeValue] = useState('');

  const freqWarning = useCommentSymbol({ componentId, symbolId: 'ADC_PRESCAL_WARNING' });

  const resultResolution = useKeyValueSetSymbol({ componentId, symbolId: 'ADC_EMR_RES_VALUE' });

  useEffect(() => {
    const temp = convTime.label.replace('**** Conversion Time is ', '').replace(' ****', '');
    setConvTimeValue(temp);
  }, [convTime.label]);

  return {
    triggerSelection,
    conversionMode,
    enableUserSequenceMode,
    clockFreq,
    freqWarning,
    prescalar,
    clockSource,
    convTime,
    convTimeValue,
    resultResolution
  };
};

export default useBlockDiagramViewModel;

export type BlockDiagramViewModel = ReturnType<typeof useBlockDiagramViewModel>;

export const BlockDiagramContext = createContext<BlockDiagramViewModel | null>(null);
