import {
  BooleanSymbol,
  ComboSymbol,
  IntegerSymbol,
  PluginConfigContext,
  StringSymbol,
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
  channelGainIds,
  channelOffsetIds,
  channelInterruptIds,
  channelDualSampleAndHoldIds
} from './ChannelConfiguration';

const useChannelConfiguration = () => {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

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
  const channelGains = useSymbols({
    componentId,
    symbolIds: channelGainIds
  }) as ComboSymbol[];
  const channelOffsets = useSymbols({
    componentId,
    symbolIds: channelOffsetIds
  }) as IntegerSymbol[];
  const channelInterrupts = useSymbols({
    componentId,
    symbolIds: channelInterruptIds
  }) as BooleanSymbol[];
  const channelDualSampleAndHolds = useSymbols({
    componentId,
    symbolIds: channelDualSampleAndHoldIds
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
      gain: channelGains[i],
      offset: channelOffsets[i],
      interrupt: channelInterrupts[i],
      dualSampleAndHold: channelDualSampleAndHolds[i],
      rowDisable: i - 1 > -1 ? channelNegativeInputs[i - 1].value !== 'GND' : false
    }));

    setChannels((e) => channels);
  }, [
    channelEnables,
    channelSignalNames,
    channelPositiveInputs,
    channelNegativeInputs,
    channelGains,
    channelOffsets,
    channelInterrupts,
    channelDualSampleAndHolds
  ]);

  return {
    channels
  };
};

export { useChannelConfiguration };
