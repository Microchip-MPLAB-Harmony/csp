import {
  GetSymbolArray,
  GetSymbolValue,
  UpdateSymbolValue,
} from "../../Common/SymbolAccess";
import { component_id } from "../MainView/MainBlock";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { convertToBoolean } from "../../Common/Utils";
import { globalSymbolSStateData } from "../../Common/UIComponents/UIComponentCommonUtils";
import GetDropDown from "../../Common/UIComponents/DropDown";
import GetInputText from "../../Common/UIComponents/InputText";
import { GetLabelWithCustomDisplayWithTooltip } from "../../Common/UIComponents/Label";
import GetCheckBox from "../../Common/UIComponents/CheckBox";
import { RowAndVectorInterruptMap } from "./Script";

const InterruptTable = (props: { parentUpdate: () => void }) => {
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < RowAndVectorInterruptMap.size; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  function GetLabel(displayValue: string, tooltip: any) {
    return (
      <div>
        <GetLabelWithCustomDisplayWithTooltip
          labelId={""}
          labelDisplayText={displayValue}
          labelStyle={null}
          labelTooltip={tooltip}
        />
      </div>
    );
  }

  const VectorNumber = (rowData: any) => {
    let symbolId = RowAndVectorInterruptMap.get(rowData.id).split("_");
    return <div>{symbolId[0]}</div>;
  };

  const VectorNameAndCaption = (rowData: any) => {
    let vectorName = GetSymbolValue(
      component_id,
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_VECTOR_NAME"
    );
    let caption = GetSymbolValue(
      component_id,
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_CAPTION"
    );
    let tooltip = caption;
    caption = String(caption);
    if (caption.length > 50) {
      caption = caption.substring(0, 50) + "...";
    }

    return (
      <div>
        {GetLabel(
          vectorName + "  (" + caption + ") ",
          "CAPTION : (" + tooltip + ")"
        )}
      </div>
    );
  };

  const EnableColumn = (rowData: any) => {
    function EnabledChangeListner(event: { value: any }) {
      // props.parentUpdate();
    }
    let symbolId =
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_ENABLE";
    let enableLock = GetSymbolValue(
      component_id,
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_ENABLE_LOCK"
    );
    return (
      <div>
        <GetCheckBox
          componentId={component_id}
          symbolId={symbolId}
          onChange={EnabledChangeListner}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={{ width: "20px", height: "20px" }}
          editable={!convertToBoolean(enableLock)}
        />
      </div>
    );
  };

  const PriorityColumn = (rowData: any) => {
    function PriorityBoxChanged(event: { value: any }) {
      let nvicId = RowAndVectorInterruptMap.get(rowData.id);
      PriorityChanged(event.value, nvicId);
    }
    let symbolID =
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_PRIORITY";
    let priorityLock = GetSymbolValue(
      component_id,
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_PRIORITY_LOCK"
    );
    return (
      <div>
        <GetDropDown
          componentId={component_id}
          symbolId={symbolID}
          onChange={PriorityBoxChanged}
          symbolValue={GetSymbolValue(component_id, symbolID)}
          symbolArray={GetSymbolArray(component_id, symbolID)}
          editable={!convertToBoolean(priorityLock)}
          styleObject={{ width: "100px", height: "35px" }}
        />
      </div>
    );
  };

  const HandlerColumn = (rowData: any) => {
    function HandlerChanged() {
      //
    }
    let handlerLock = GetSymbolValue(
      component_id,
      "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_HANDLER_LOCK"
    );
    return (
      <div className="p-d-flex">
        <GetInputText
          component_id={component_id}
          symbolId={
            "NVIC_" + RowAndVectorInterruptMap.get(rowData.id) + "_HANDLER"
          }
          width="250px"
          onChange={HandlerChanged}
          editable={!convertToBoolean(handlerLock)}
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
            size="small"
            resizableColumns
            scrollHeight="flex"
            showGridlines
            responsiveLayout="scroll"
            columnResizeMode="expand"
          >
            <Column
              field="Vector Number"
              header="Vector Number"
              body={VectorNumber}
            ></Column>
            <Column
              field="Vector"
              header="Vector"
              body={VectorNameAndCaption}
            ></Column>
            <Column
              field="Enable"
              header="Enable"
              body={EnableColumn}
              style={{ width: "100px" }}
            ></Column>
            <Column
              field="Priority (0 = Highest)"
              header="Priority (0 = Highest)"
              body={PriorityColumn}
              style={{ width: "150px" }}
            ></Column>
            <Column
              field="HandlerName"
              header="HandlerName"
              body={HandlerColumn}
            ></Column>
          </DataTable>
        </div>
      </div>
    </div>
  );
};
export default InterruptTable;

export function PriorityChanged(symbolValue: any, nvicId: any) {
  try {
    let szCheckString = nvicId.split("_")[0] + "_";
    for (let i = 0; i < RowAndVectorInterruptMap.size; i++) {
      let value = RowAndVectorInterruptMap.get(i);
      if (value.startsWith(szCheckString)) {
        globalSymbolSStateData
          .get("NVIC_" + value + "_PRIORITY")
          .changeValue(symbolValue);
        UpdateSymbolValue(
          component_id,
          "NVIC_" + value + "_PRIORITY",
          symbolValue
        );
      }
    }
  } catch (err) {
    alert(err);
  }
}
