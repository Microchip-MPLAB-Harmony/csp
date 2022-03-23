import { GetSymbolValue, GetSymbolArray } from "../../Common/SymbolAccess";
import { component_id } from "../MainView/MainBlock";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import {
  GetLabelWithCustomDisplay,
  GetUIComponentWithOutLabel,
} from "../../Common/UIComponent";

const GenericClockConfiguration = (props: { parentUpdate: () => void }) => {
  let channelPeripipheralMap = GetSymbolArray(
    component_id,
    "GCLK_INSTANCE_PID"
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
    return <div>{channelPeripipheralMap[rowData.id]}</div>;
  };

  const EnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={"CLK_" + channelPeripipheralMap[rowData.id] + "_GCLKEN"}
          onChange={props.parentUpdate}
        />
      </div>
    );
  };

  const SourceBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={"CLK_" + channelPeripipheralMap[rowData.id] + "_GCLKCSS"}
          onChange={props.parentUpdate}
        />
      </div>
    );
  };

  const DivisorBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetUIComponentWithOutLabel
          componentId={component_id}
          symbolId={"CLK_" + channelPeripipheralMap[rowData.id] + "_GCLKDIV"}
          onChange={props.parentUpdate}
        />
      </div>
    );
  };

  const FrequencyBodyTemplate = (rowData: any) => {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={channelPeripipheralMap[rowData.id] + "_GCLK_FREQUENCY"}
          labelDisplayText={
            GetSymbolValue(
              component_id,
              channelPeripipheralMap[rowData.id] + "_GCLK_FREQUENCY"
            ) + " Hz"
          }
          labelStyle={null}
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
            style={{width:"650px"}}
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
            <Column
              field="Source"
              header="Source"
              body={SourceBodyTemplate}
            ></Column>
            <Column
              field="Divisor"
              header="Divisor"
              body={DivisorBodyTemplate}
            ></Column>
            <Column
              field="Frequency"
              header="Frequency"
              body={FrequencyBodyTemplate}
            ></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default GenericClockConfiguration;
