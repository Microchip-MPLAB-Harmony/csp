import { useContext, useEffect, useState } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import styles from './channel-configuration.module.css';
import {
  useBooleanSymbol,
  CheckBox,
  InputTextDefault,
  useStringSymbol,
  useComboSymbol,
  ComboBox,
  CheckBoxDefault,
  PluginConfigContext,
  createClassResolver,
  InputNumber,
  useIntegerSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { ChannelId, initialChannelIds, initialRowDisables } from './ChannelConfiguration';

const cx = createClassResolver(styles);

export default function ChannelConfigurationView() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const [channels, setChannels] = useState<ChannelId[]>(initialChannelIds);

  const [rowDisable, setRowDisable] = useState<boolean[]>(initialRowDisables);

  useEffect(() => {
    const temp = channels.map((channel) => {
      channel.toolTip =
        rowDisable[channel.channelNumber] === true
          ? `AN${channel.channelNumber} is used as negative input of Channel ${
              channel.channelNumber - 1
            }`
          : '';
      return channel;
    });
    setChannels(temp);
  }, [rowDisable]);

  const ChannelCell = (channel: ChannelId) => {
    return <label style={{ whiteSpace: 'nowrap' }}>{channel.name}</label>;
  };

  const EnableCell = (channel: ChannelId) => {
    const symbol = useBooleanSymbol({ componentId, symbolId: channel.enable });

    return (
      <CheckBox
        booleanSymbolHook={symbol}
        hidden={false}
        disabled={rowDisable[channel.channelNumber]}
        tooltip={channel.toolTip}
      />
    );
  };

  const SignalNameCell = (channel: ChannelId) => {
    return (
      <InputTextDefault
        componentId={componentId}
        symbolId={channel.signalName}
        hidden={false}
        disabled={rowDisable[channel.channelNumber]}
        tooltip={channel.toolTip}
        tooltipOptions={{ showOnDisabled: true }}
        style={{ width: '100%' }}
      />
    );
  };

  const PositiveInputCell = (channel: ChannelId) => {
    const positiveInput = useStringSymbol({ componentId, symbolId: channel.positiveInput });
    return <label style={{ whiteSpace: 'nowrap' }}>{positiveInput.value}</label>;
  };

  const NegativeInputCell = (channel: ChannelId) => {
    const symbol = useComboSymbol({ componentId, symbolId: channel.negativeInput });

    useEffect(() => {
      if (symbol.value !== 'GND') {
        setRowDisable(rowDisable.map((e, i) => (i === channel.channelNumber + 1 ? true : e)));
      } else {
        setRowDisable(rowDisable.map((e, i) => (i === channel.channelNumber + 1 ? false : e)));
      }
    }, [symbol.value]);
    return (
      <ComboBox
        comboSymbolHook={symbol}
        hidden={false}
        style={{ width: '100%' }}
        tooltip={channel.toolTip}
        tooltipOptions={{ showOnDisabled: true }}
        disabled={rowDisable[channel.channelNumber] || symbol.readOnly || !symbol.visible}
      />
    );
  };

  const GainCell = (channel: ChannelId) => {
    const symbol = useComboSymbol({ componentId, symbolId: channel.gain });

    return (
      <ComboBox
        comboSymbolHook={symbol}
        hidden={false}
        style={{ width: '100%' }}
        tooltip={channel.toolTip}
        tooltipOptions={{ showOnDisabled: true }}
        disabled={rowDisable[channel.channelNumber] || symbol.readOnly || !symbol.visible}
      />
    );
  };

  const OffsetCell = (channel: ChannelId) => {
    const symbol = useIntegerSymbol({ componentId, symbolId: channel.offset });

    return (
      <InputNumber
        integerSymbolHook={symbol}
        hidden={false}
        style={{ width: '100%' }}
        tooltip={channel.toolTip}
        tooltipOptions={{ showOnDisabled: true }}
        disabled={rowDisable[channel.channelNumber] || symbol.readOnly || !symbol.visible}
      />
    );
  };

  const InterruptCell = (channel: ChannelId) => {
    return (
      <CheckBoxDefault
        componentId={componentId}
        symbolId={channel.interrupt}
        hidden={false}
        tooltip={channel.toolTip}
        tooltipOptions={{ showOnDisabled: true }}
        disabled={rowDisable[channel.channelNumber]}
      />
    );
  };

  const DualSampleAndHoldCell = (channel: ChannelId) => {
    if (channel.channelNumber < 6) {
      return (
        <CheckBoxDefault
          componentId={componentId}
          symbolId={channel.dualSampleAndHold}
          hidden={false}
          tooltip={channel.toolTip}
          tooltipOptions={{ showOnDisabled: true }}
          disabled={rowDisable[channel.channelNumber]}
        />
      );
    } else {
      return <div></div>;
    }
  };

  return (
    <DataTable
      className={cx('channel-configuration-table')}
      value={channels}>
      <Column
        field='name'
        header='Channel'
        headerStyle={{ width: 80, textAlign: 'center' }}
        body={ChannelCell}></Column>
      <Column
        field='enable'
        header='Enable'
        headerStyle={{ width: 100 }}
        align='center'
        body={EnableCell}></Column>
      <Column
        field='signalName'
        header='Signal Name'
        headerStyle={{ width: 200 }}
        align='center'
        body={SignalNameCell}></Column>
      <Column
        field='positiveInput'
        header='Positive Input'
        headerStyle={{ width: 100 }}
        align='center'
        body={PositiveInputCell}></Column>
      <Column
        field='negativeInput'
        header='Negative Input'
        headerStyle={{ width: 140 }}
        align='center'
        body={NegativeInputCell}></Column>
      <Column
        field='gain'
        header='Gain'
        headerStyle={{ width: 140 }}
        align='center'
        body={GainCell}></Column>
      <Column
        field='offset'
        header='Offset'
        headerStyle={{ width: 140 }}
        align='center'
        body={OffsetCell}></Column>
      <Column
        field='interrupt'
        header='Interrupt'
        headerStyle={{ width: 100 }}
        align='center'
        body={InterruptCell}></Column>
      <Column
        field='dualSampleAndHold'
        header='Dual Sample/Hold'
        headerStyle={{ width: 120 }}
        align='center'
        body={DualSampleAndHoldCell}></Column>
    </DataTable>
  );
}
