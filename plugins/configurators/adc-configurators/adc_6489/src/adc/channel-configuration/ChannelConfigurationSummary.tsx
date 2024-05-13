import { useEffect, useState } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import styles from './channel-configuration.module.css';
import { createClassResolver } from '@mplab_harmony/harmony-plugin-client-lib';
import { useChannelConfiguration } from './useChannelConfiguration';
import { Channel } from './ChannelConfiguration';

const cx = createClassResolver(styles);

export default function ChannelConfigurationSummary() {
  const { diffSettings, channels } = useChannelConfiguration();

  const [filteredChannels, setFilteredSymbols] = useState<Channel[]>([]);

  useEffect(() => {
    console.log(`channels.length ${channels.length}`);
    if (channels.length === 0) return;

    setFilteredSymbols(
      channels
        .filter((e) => (e.enable !== undefined ? e.enable.value : false))
        .filter((e) => e.rowDisable === false)
    );
  }, [channels]);

  const ChannelCell = (channel: Channel) => {
    return <label style={{ whiteSpace: 'nowrap' }}>{channel.name}</label>;
  };

  const EnableCell = (channel: Channel) => {
    if (channel.enable?.value) {
      return (
        <i
          className='pi pi-check'
          style={{ color: 'green', fontSize: '1.25rem' }}></i>
      );
    } else {
      return (
        <i
          className='pi pi-times'
          style={{ color: 'red', fontSize: '1.25rem' }}></i>
      );
    }
  };

  const SignalNameCell = (channel: Channel) => {
    return (
      <label>{channel.signalName !== undefined ? channel.signalName.value : 'loading...'}</label>
    );
  };

  const PositiveInputCell = (channel: Channel) => {
    return (
      <label style={{ whiteSpace: 'nowrap' }}>
        {channel.positiveInput !== undefined ? channel.positiveInput.value : 'loading...'}
      </label>
    );
  };

  const NegativeInputCell = (channel: Channel) => {
    return (
      <label style={{ whiteSpace: 'nowrap' }}>
        {channel.negativeInput !== undefined ? channel.negativeInput.value : 'loading...'}
      </label>
    );
  };

  const InterruptCell = (channel: Channel) => {
    if (channel.interrupt?.value) {
      return (
        <i
          className='pi pi-check'
          style={{ color: 'green', fontSize: '1.25rem' }}></i>
      );
    } else {
      return (
        <i
          className='pi pi-ban'
          style={{ color: 'orange', fontSize: '1.25rem' }}></i>
      );
    }
  };

  return (
    <>
      {diffSettings.value ? (
        <i
          className='pi pi-check'
          style={{ color: 'green', fontSize: '1.25rem', margin: 10 }}></i>
      ) : (
        <i
          className='pi pi-ban'
          style={{ color: 'orange', fontSize: '1.25rem', margin: 10 }}></i>
      )}
      <label>{diffSettings.label}</label>
      <div className={cx('channel-configuration-table')}>
        <DataTable value={filteredChannels}>
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
            field='interrupt'
            header='Interrupt'
            headerStyle={{ width: 100 }}
            align='center'
            body={InterruptCell}></Column>
        </DataTable>
      </div>
    </>
  );
}
