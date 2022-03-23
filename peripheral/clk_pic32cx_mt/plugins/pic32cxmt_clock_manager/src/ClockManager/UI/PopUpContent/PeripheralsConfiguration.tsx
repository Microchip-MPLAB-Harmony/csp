import {
  GetSymbolLabelName,
  GetSymbolArray,
} from "../../Common/SymbolAccess";
import { component_id } from "../MainView/MainBlock";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import {
  GetUIComponentWithOutLabel,
} from "../../Common/UIComponent";

const PeripheralsConfiguration = (props: { parentUpdate: () => void }) => {
  let channelPeripipheralMap = GetSymbolArray(
    component_id,
    "PERIPHERAL_CLOCK_CONFIG"
  );
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < channelPeripipheralMap.length; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const PeripheralBodyTemplate = (rowData: any) => {
    return (
      <div>
        {GetSymbolLabelName(component_id, channelPeripipheralMap[rowData.id])}
      </div>
    );
  };

  const EnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={channelPeripipheralMap[rowData.id]}
          onChange={props.parentUpdate}
        />
      </div>
    );
  };

  return (
    <div>
      <div className="p-d-flex">
        <div className="card">
          <DataTable
            value={customLabelsArray}
            stripedRows
            showGridlines
            responsiveLayout="scroll"
            style={{width:"400px"}}
          >
            <Column
              field="Peripheral"
              header="Peripheral"
              body={PeripheralBodyTemplate}
            ></Column>
            <Column
              field="Enable"
              header="Enable"
              body={EnableBodyTemplate}
            ></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default PeripheralsConfiguration;