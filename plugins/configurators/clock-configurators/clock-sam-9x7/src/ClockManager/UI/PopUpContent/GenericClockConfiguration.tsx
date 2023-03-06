import { component_id } from '../MainView/MainBlock';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import {
  GetSymbolArray,
  GetSymbolValue
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { GetLabelWithCustomDisplay } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';

const GenericClockConfiguration = (props: { parentUpdate: () => void }) => {
  const channelPeripipheralMap = GetSymbolArray(component_id, 'GCLK_INSTANCE_PID');
  const customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    const dataArr = [];
    for (let i = 0; i < channelPeripipheralMap.length; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const PeripheralBodyTemplate = (rowData: any) => {
    return <div>{channelPeripipheralMap[rowData.id]}</div>;
  };

  const EnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKEN'}
          onChange={props.parentUpdate}
          symbolListeners={['CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKEN']}
        />
      </div>
    );
  };

  const SourceBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKCSS'}
          onChange={props.parentUpdate}
          symbolListeners={['CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKCSS']}
        />
      </div>
    );
  };

  const DivisorBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={'CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKDIV'}
          onChange={props.parentUpdate}
          symbolListeners={['CLK_' + channelPeripipheralMap[rowData.id] + '_GCLKDIV']}
        />
      </div>
    );
  };

  const FrequencyBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={channelPeripipheralMap[rowData.id] + '_GCLK_FREQUENCY'}
          labelDisplayText={
            GetSymbolValue(component_id, channelPeripipheralMap[rowData.id] + '_GCLK_FREQUENCY') +
            ' Hz'
          }
          labelStyle={null}
        />
      </div>
    );
  };

  return (
    <div>
      <div className='flex'>
        <div className='card'>
          <DataTable
            value={customLabelsArray}
            stripedRows
            showGridlines
            responsiveLayout='scroll'>
            <Column
              field='Peripheral'
              header='Peripheral'
              body={PeripheralBodyTemplate}></Column>
            <Column
              field='Enable'
              header='Enable'
              body={EnableBodyTemplate}></Column>
            <Column
              field='Source'
              header='Source'
              body={SourceBodyTemplate}></Column>
            <Column
              field='Divisor'
              header='Divisor'
              body={DivisorBodyTemplate}></Column>
            <Column
              field='Frequency'
              header='Frequency'
              body={FrequencyBodyTemplate}></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default GenericClockConfiguration;
