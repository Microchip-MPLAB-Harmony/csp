import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import {
  BooleanSymbol,
  CheckBoxDefault,
  PluginConfigContext,
  symbolUtilApi
} from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useEffect, useState } from 'react';

interface Sequence {
  label: string;
  sequenceId: string;
}

const getSequences = async (componentId: string) => {
  const childrenIds = await symbolUtilApi.getChildren(componentId, 'ADC_SEQ_ENABLE');

  const sequenceSymbols = (await symbolUtilApi.getSymbols(
    componentId,
    childrenIds
  )) as BooleanSymbol[];

  return sequenceSymbols.map(
    (symbol) => ({ label: symbol.label, sequenceId: symbol.symbolId } as Sequence)
  );
};

export default function ChannelSequence() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const [sequences, setSequences] = useState<Sequence[]>([]);

  useEffect(() => {
    getSequences(componentId).then((e) => setSequences(e));
  }, []);

  const PinNameCell = (userSequence: Sequence) => {
    return <label style={{ whiteSpace: 'nowrap' }}>{userSequence.label}</label>;
  };

  const EnableCell = (userSequence: Sequence) => {
    return (
      <CheckBoxDefault
        componentId={componentId}
        symbolId={userSequence.sequenceId}
        style={{ width: '100%' }}
        hidden={false}
      />
    );
  };

  return (
    <div className='channel-sequence-table'>
      <DataTable
        value={sequences}
        scrollable
        scrollHeight='400px'
        loading={sequences.length === 0}>
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
