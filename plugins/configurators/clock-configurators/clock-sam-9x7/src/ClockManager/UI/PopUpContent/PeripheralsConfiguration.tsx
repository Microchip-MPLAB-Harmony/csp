import { component_id } from '../MainView/MainBlock';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import {
  GetSymbolArray,
  GetSymbolLabelName
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

const PeripheralsConfiguration = () => {
  const channelPeripipheralMap = GetSymbolArray(component_id, 'PERIPHERAL_CLOCK_CONFIG');
  const customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    const dataArr = [];
    for (let i = 0; i < channelPeripipheralMap.length; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const PeripheralBodyTemplate = (rowData: any) => {
    return <div>{GetSymbolLabelName(component_id, channelPeripipheralMap[rowData.id])}</div>;
  };

  function ValueChange(onChangeData: Map<String, any>) {
    // do nothing
  }

  const EnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={channelPeripipheralMap[rowData.id]}
          onChange={ValueChange}
          symbolListeners={[channelPeripipheralMap[rowData.id]]}
        />
      </div>
    );
  };

  return (
    <div>
      <div className='p-d-flex'>
        <div className='card'>
          <DataTable
            value={customLabelsArray}
            stripedRows
            showGridlines
            responsiveLayout='scroll'
            style={{ width: '400px' }}>
            <Column
              field='Peripheral'
              header='Peripheral'
              body={PeripheralBodyTemplate}></Column>
            <Column
              field='Enable'
              header='Enable'
              body={EnableBodyTemplate}></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default PeripheralsConfiguration;
