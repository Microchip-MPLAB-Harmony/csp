import {
  BooleanSymbol,
  ComboSymbol,
  PluginConfigContext,
  StringSymbol,
  useBooleanSymbol,
  useSymbols
} from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useEffect, useState } from 'react';
import {
  Channel,
  initialChannelIds,
  channelEnableIds,
  channelSignalNameIds,
  channelPositiveInputIds,
  channelNegativeInputIds,
  channelInterruptIds
} from './ChannelConfiguration';

const useChannelConfiguration = () => {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const diffSettings = useBooleanSymbol({ componentId, symbolId: 'ADC_MR_ANACH' });

  const [channels, setChannels] = useState<Channel[]>([]);

  const channelEnables = useSymbols({
    componentId,
    symbolIds: channelEnableIds
  }) as BooleanSymbol[];
  const channelSignalNames = useSymbols({
    componentId,
    symbolIds: channelSignalNameIds
  }) as StringSymbol[];
  const channelPositiveInputs = useSymbols({
    componentId,
    symbolIds: channelPositiveInputIds
  }) as StringSymbol[];
  const channelNegativeInputs = useSymbols({
    componentId,
    symbolIds: channelNegativeInputIds
  }) as ComboSymbol[];
  const channelInterrupts = useSymbols({
    componentId,
    symbolIds: channelInterruptIds
  }) as BooleanSymbol[];

  useEffect(() => {
    if (channelInterrupts === undefined || channelInterrupts.length === 0) return;
    if (!channelInterrupts.every((e) => e !== undefined)) return;

    const channels: Channel[] = initialChannelIds.map((e, i) => ({
      channelNumber: i,
      name: e.name,
      enable: channelEnables[i],
      signalName: channelSignalNames[i],
      positiveInput: channelPositiveInputs[i],
      negativeInput: channelNegativeInputs[i],
      interrupt: channelInterrupts[i],
      rowDisable: i - 1 > -1 ? channelNegativeInputs[i - 1].value !== 'GND' : false
    }));

    setChannels((e) => channels);
  }, [
    channelEnables,
    channelSignalNames,
    channelPositiveInputs,
    channelNegativeInputs,
    channelInterrupts
  ]);

  return {
    diffSettings,
    channels
  };
};

export { useChannelConfiguration };
