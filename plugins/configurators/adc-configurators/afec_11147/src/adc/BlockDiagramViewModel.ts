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

  const clockFreq = useIntegerSymbol({ componentId, symbolId: 'AFEC_CLK' });
  const prescalar = useIntegerSymbol({ componentId, symbolId: 'AFEC_MR_PRESCAL' });

  const enableUserSequenceMode = useBooleanSymbol({ componentId, symbolId: 'AFEC_MR_USEQ' });
  const triggerSelection = useKeyValueSetSymbol({ componentId, symbolId: 'AFEC_MR_TRGSEL_VALUE' });

  const conversionMode = useKeyValueSetSymbol({ componentId, symbolId: 'AFEC_CONV_MODE' });

  const convTime = useCommentSymbol({ componentId, symbolId: 'AFEC_CONV_TIME' });
  const [convTimeValue, setConvTimeValue] = useState('');

  const freqWarning = useCommentSymbol({ componentId, symbolId: 'AFEC_PRESCAL_WARNING' });

  const resultResolution = useKeyValueSetSymbol({ componentId, symbolId: 'AFEC_EMR_RES_VALUE' });
  const resultSign = useKeyValueSetSymbol({ componentId, symbolId: 'AFEC_EMR_SIGNMODE_VALUE' });

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
    convTime,
    convTimeValue,
    resultResolution,
    resultSign
  };
};

export default useBlockDiagramViewModel;

export type BlockDiagramViewModel = ReturnType<typeof useBlockDiagramViewModel>;

export const BlockDiagramContext = createContext<BlockDiagramViewModel | null>(null);
