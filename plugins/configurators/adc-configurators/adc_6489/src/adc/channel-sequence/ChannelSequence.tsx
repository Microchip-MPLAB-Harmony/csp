import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { ComboBoxDefault, PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext } from 'react';

const CHANNEL_MAX = 7;

interface UserSequence {
  label: string;
  channelSelector: string;
}

function createInitialUserSequences() {
  const userSequences: UserSequence[] = [];
  for (let i = 1; i <= CHANNEL_MAX; i++) {
    userSequences.push({
      label: 'Sequence Number ' + i,
      channelSelector: `ADC_SEQ1R_USCH${i - 1}`
    });
  }
  return userSequences;
}

const userSequences = createInitialUserSequences();

const channelSelectorIds = userSequences.map((e) => e.channelSelector);

export default function ChannelSequence() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const getSequenceNumberCell = (userSequence: UserSequence) => {
    return <label style={{ whiteSpace: 'nowrap' }}>{userSequence.label}</label>;
  };

  const getChannelCell = (userSequence: UserSequence) => {
    return (
      <ComboBoxDefault
        componentId={componentId}
        symbolId={userSequence.channelSelector}
        style={{ width: '100%' }}
        hidden={false}
      />
    );
  };

  return (
    <div className='channel-sequence-table'>
      <DataTable
        value={userSequences}
        scrollable
        scrollHeight='400px'>
        <Column
          field='label'
          header='Sequence Number'
          headerStyle={{ width: 220 }}
          body={getSequenceNumberCell}></Column>
        <Column
          field='channelSelector'
          header='Channel'
          body={getChannelCell}></Column>
      </DataTable>
    </div>
  );
}

export { userSequences, channelSelectorIds };

export type { UserSequence };
