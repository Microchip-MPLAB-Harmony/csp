import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import {
  BooleanSymbol,
  EventAgentContext,
  PluginConfigContext,
  symbolUtilApi,
  toSymbolStateListener,
  toSymbolValueListener,
  toSymbolVisibleListener,
  useBooleanSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useEffect, useState } from 'react';

interface Sequence {
  label: string;
  sequenceId: string;
}

export default function ChannelSequenceSummary() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);
  const eventAgent = useContext(EventAgentContext);

  const [sequences, setSequences] = useState<Sequence[]>([]);

  useEffect(() => {
    refreshFilteredSequences();

    const valueListener = toSymbolValueListener(onSymbolChanged, { componentId });
    const visibilityListener = toSymbolVisibleListener(onSymbolChanged, { componentId });
    const stateListener = toSymbolStateListener(onSymbolChanged, { componentId });

    eventAgent.addEventListener(valueListener);
    eventAgent.addEventListener(visibilityListener);
    eventAgent.addEventListener(stateListener);

    return () => {
      eventAgent.removeEventListener(valueListener);
      eventAgent.removeEventListener(visibilityListener);
      eventAgent.removeEventListener(stateListener);
    };
  }, []);

  const refreshFilteredSequences = async () => {
    const childrenIds = await symbolUtilApi.getChildren(componentId, 'ADC_SEQ_ENABLE');

    const sequenceSymbols = (await symbolUtilApi.getSymbols(
      componentId,
      childrenIds
    )) as BooleanSymbol[];

    setSequences(
      sequenceSymbols
        .filter((e) => e.value)
        .map((symbol) => ({ label: symbol.label, sequenceId: symbol.symbolId } as Sequence))
    );
  };

  const onSymbolChanged = async (event: any) => {
    refreshFilteredSequences();
  };

  const PinNameCell = (userSequence: Sequence) => {
    return <label style={{ whiteSpace: 'nowrap' }}>{userSequence.label}</label>;
  };

  const EnableCell = (userSequence: Sequence) => {
    const { value } = useBooleanSymbol({ componentId, symbolId: userSequence.sequenceId });

    if (value) {
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
    <div className='channel-sequence-table'>
      <DataTable
        value={sequences}
        scrollable
        scrollHeight='400px'
        emptyMessage='No Channel Sequences are enabled'>
        <Column
          field='label'
          header='Pin Name'
          headerStyle={{ width: 340 }}
          body={PinNameCell}></Column>
        <Column
          field='sequenceId'
          header='Enable'
          body={EnableCell}></Column>
      </DataTable>
    </div>
  );
}
