import { BooleanSymbol, ComboSymbol, StringSymbol } from '@mplab_harmony/harmony-plugin-client-lib';

const CHANNEL_MAX = 8;

interface Channel {
  channelNumber: number;
  name: string;
  enable: BooleanSymbol;
  signalName: StringSymbol;
  positiveInput: StringSymbol;
  negativeInput: ComboSymbol;
  interrupt: BooleanSymbol;
  rowDisable: boolean;
}

interface ChannelId {
  channelNumber: number;
  name: string;
  enable: string;
  signalName: string;
  positiveInput: string;
  negativeInput: string;
  interrupt: string;
  toolTip: string;
}

function createInitialChannelIds() {
  const channelIds: ChannelId[] = [];
  for (let i = 0; i < CHANNEL_MAX; i++) {
    channelIds.push({
      channelNumber: i,
      name: 'CH' + i,
      enable: `ADC_${i}_CHER`,
      signalName: `ADC_${i}_NAME`,
      positiveInput: `ADC_${i}_POS_INP`,
      negativeInput: `ADC_${i}_NEG_INP`,
      interrupt: `ADC_${i}_IER_EOC`,
      toolTip: ''
    });
  }
  return channelIds;
}

const initialChannelIds = createInitialChannelIds();

function createInitialRowDisables() {
  const rowDisable: boolean[] = [];
  for (let i = 0; i < CHANNEL_MAX; i++) {
    rowDisable.push(false);
  }
  return rowDisable;
}

const initialRowDisables = createInitialRowDisables();

const channelEnableIds = initialChannelIds.map((e) => e.enable);
const channelSignalNameIds = initialChannelIds.map((e) => e.signalName);
const channelPositiveInputIds = initialChannelIds.map((e) => e.positiveInput);
const channelNegativeInputIds = initialChannelIds.map((e) => e.negativeInput);
const channelInterruptIds = initialChannelIds.map((e) => e.interrupt);

export {
  initialChannelIds,
  initialRowDisables,
  channelEnableIds,
  channelSignalNameIds,
  channelPositiveInputIds,
  channelNegativeInputIds,
  channelInterruptIds
};

export type { Channel, ChannelId };
