import React, { useState } from "react";
import { ListBox } from "primereact/listbox";
import {
  GetLabelWithCustomDisplay,
  GetStyle,
  GetUIComponentWithOutLabel,
  GetDropDown,
  GetInputNumber,
  GetCheckBox,
  GetMinFractionValueBasedSymbolType,
} from "../../Common/UIComponent";
import { component_id } from "./MainBlock";
import {
  GetSymbolArray,
  GetSymbolMaxValue,
  GetSymbolMinValue,
  GetSymbolValue,
} from "../../Common/SymbolAccess";
import { AddBoldLabel, AddDivioType, CheckSelectedSymbolValue } from "./CustomLabels";

const ProgrammableClockController = (props: { parentUpdate: () => void }) => {
  const [value, setValue] = useState("PLCK 0");
  const tabs = ["PLCK 0", "PLCK 1"];

  function AddPLCK(index: number) {
    return (
        <div className="p-fluid">
        {AddCombobox("CLK_PCK" + index + "_CSS", "CLK_PCK0_CSS")}
        {AddInputNumber("CLK_PCK" + index + "_PRES", "CLK_PCK0_PRES")}
        {AddCheckBox("CLK_PCK" + index + "_EN", "CLK_PCK0_EN")}
        {AddFrequencyLabel(
          "CLK_PCK" + index + "_FREQUENCY",
          "CLK_PCK0_FREQUENCY"
        )}

        {AddDivioType(
          "label_pclkPresVal",
          GetSymbolValue(component_id, "CLK_PCK" + index + "_PRES")
        )}

        {AddBoldLabel(
          "label_pclk_MD_SLCK",
          "MD_CLK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "MD_SLOW_CLK")
        )}
        {AddBoldLabel(
          "label_pclk_TD_SLCK",
          "TD_SLCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "TD_SLOW_CLOCK")
        )}
        {AddBoldLabel(
          "label_pclk_MAINCK",
          "MAINCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "MAINCK")
        )}
        {AddBoldLabel(
          "label_pclk_MANCK",
          "MCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "MCK")
        )}
        {AddBoldLabel(
          "label_pclk_PLLACK",
          "PLLACK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "PLLA")
        )}
        {AddBoldLabel(
          "label_pclk_UPLLCK",
          "UPLLCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "UPLL")
        )}
        {AddBoldLabel(
          "label_pclk_AUDIOPLLCK",
          "AUDIOPLLCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "AUDIOPLL")
        )}
      </div>
    );
  }

  function AddFrequencyLabel(symbolId: string, styleId: string) {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={symbolId}
          labelDisplayText={GetSymbolValue(component_id, symbolId) + " Hz"}
          labelStyle={GetStyle(styleId)}
        />
      </div>
    );
  }

  function AddCombobox(symbolId: string, styleId: string) {
    return (
      <div>
        <GetDropDown
          componentId={component_id}
          symbolId={symbolId}
          onChange={props.parentUpdate}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
        />
      </div>
    );
  }

  function AddCheckBox(symbolId: string, styleId: string) {
    return (
      <div>
        <GetCheckBox
          componentId={component_id}
          symbolId={symbolId}
          onChange={props.parentUpdate}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
        />
      </div>
    );
  }

  function AddInputNumber(symbolId: string, styleId: string) {
    return (
      <div>
        <GetInputNumber
          componentId={component_id}
          symbolId={symbolId}
          onChange={props.parentUpdate}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          minFractionValue={GetMinFractionValueBasedSymbolType(
            component_id,
            symbolId
          )}
          minValue={GetSymbolMinValue(component_id, symbolId)}
          maxValue={GetSymbolMaxValue(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
        />
      </div>
    );
  }

  function NullSelected(){
    setValue("PLCK 0");
    return(<div>
        {AddPLCK(0)}
    </div>);
  }

  return (
    <div className="card">
      <ListBox
        value={value}
        options={tabs}
        style={GetStyle("button_pclkTab0")}
        onChange={(e) => setValue(e.value)}
      />
      {!value && NullSelected()}
      {value === "PLCK 0" && AddPLCK(0)}
      {value === "PLCK 1" && AddPLCK(1)}
    </div>
  );
};

export default ProgrammableClockController;
