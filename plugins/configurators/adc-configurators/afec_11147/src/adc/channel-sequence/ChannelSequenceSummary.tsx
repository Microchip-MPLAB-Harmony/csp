import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import {
  ComboSymbol,
  PluginConfigContext,
  useBooleanSymbol,
  useSymbols
} from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useEffect, useState } from 'react';
import { channelSelectorIds, userSequences } from './ChannelSequence';

function getSuffixDigitsAsNumber(value: string) {
  if (value === undefined) {
    return 69696;
  }
  const matches = value.match(/(\d+)$/);
  if (matches) {
    return parseInt(matches[1], 10);
  }
  return 69696;
}

export default function ChannelSequenceSummary() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const enableUserSequenceMode = useBooleanSymbol({ componentId, symbolId: 'AFEC_MR_USEQ' });

  const symbols = useSymbols({ componentId, symbolIds: channelSelectorIds }) as ComboSymbol[];

  const [filteredSymbols, setFilteredSymbols] = useState<ComboSymbol[]>([]);

  useEffect(() => {
    setFilteredSymbols(symbols.filter((e) => e.value !== 'NONE'));
  }, [symbols]);

  const SequenceNumberCell = (symbol: ComboSymbol) => {
    return (
      <label style={{ whiteSpace: 'nowrap' }}>
        {'Sequence Number ' + getSuffixDigitsAsNumber(symbol.label)}
      </label>
    );
  };

  const ChannelCell = (symbol: ComboSymbol) => {
    return <label style={{ width: '100%' }}>{symbol.value}</label>;
  };

  return (
    <div className='channel-sequence-table'>
      {!enableUserSequenceMode.value && (
        <div>
          <i
            className='pi pi-ban'
            style={{ color: 'orange', fontSize: '1.25rem', margin: 10 }}></i>
          <label>User Sequence Mode is disabled.</label>
        </div>
      )}
      {enableUserSequenceMode.value && (
        <DataTable
          value={filteredSymbols}
          scrollable
          scrollHeight='400px'>
          <Column
            field='label'
            header='Sequence Number'
            headerStyle={{ width: 220 }}
            body={SequenceNumberCell}></Column>
          <Column
            field='channelSelector'
            header='Channel'
            body={ChannelCell}></Column>
        </DataTable>
      )}
    </div>
  );
}

export { userSequences };
