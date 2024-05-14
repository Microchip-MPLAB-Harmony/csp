import {
  BooleanSymbol,
  ComboSymbol,
  IntegerSymbol,
  StringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';

const CHANNEL_MAX = 12;

interface Channel {
  channelNumber: number;
  name: string;
  enable: BooleanSymbol;
  signalName: StringSymbol;
  positiveInput: StringSymbol;
  negativeInput: ComboSymbol;
  gain: ComboSymbol;
  offset: IntegerSymbol;
  interrupt: BooleanSymbol;
  dualSampleAndHold: BooleanSymbol;
  rowDisable: boolean;
}

interface ChannelId {
  channelNumber: number;
  name: string;
  enable: string;
  signalName: string;
  positiveInput: string;
  negativeInput: string;
  gain: string;
  offset: string;
  interrupt: string;
  dualSampleAndHold: string;
  toolTip: string;
}

function createInitialChannelIds() {
  const channelIds: ChannelId[] = [];
  for (let i = 0; i < CHANNEL_MAX; i++) {
    channelIds.push({
      channelNumber: i,
      name: 'CH' + i,
      enable: `AFEC_${i}_CHER`,
      signalName: `AFEC_${i}_NAME`,
      positiveInput: `AFEC_${i}_POS_INP`,
      negativeInput: `AFEC_${i}_NEG_INP`,
      gain: `AFEC_${i}_CGR_GAIN`,
      offset: `AFEC_${i}_COCR_AOFF`,
      interrupt: `AFEC_${i}_IER_EOC`,
      dualSampleAndHold: `AFEC_${i}_SHMR_DUAL`,
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
const channelGainIds = initialChannelIds.map((e) => e.gain);
const channelOffsetIds = initialChannelIds.map((e) => e.offset);
const channelInterruptIds = initialChannelIds.map((e) => e.interrupt);
const channelDualSampleAndHoldIds = initialChannelIds.map((e) => e.dualSampleAndHold);

export {
  initialChannelIds,
  initialRowDisables,
  channelEnableIds,
  channelSignalNameIds,
  channelPositiveInputIds,
  channelNegativeInputIds,
  channelGainIds,
  channelOffsetIds,
  channelInterruptIds,
  channelDualSampleAndHoldIds
};

export type { Channel, ChannelId };
