import React, { useState } from "react";
import { ListBox } from "primereact/listbox";
import {
  GetStyle
} from "../../../Common/UIComponent";
import { component_id } from "../MainBlock";
import {
  GetSymbolValue,
} from "../../../Common/SymbolAccess";
import { CheckSelectedSymbolValue } from "../CoreCustomLabels";
import { AddBoldLabel, AddCheckBox, AddCombobox, AddDivioType, AddFrequencyLabel, AddInputNumber } from "../../../Common/ClockCommonUtils";

const ProgrammableClockController = (props: { parentUpdate: () => void }) => {
  const [value, setValue] = useState("PLCK 0");
  const tabs = ["PLCK 0", "PLCK 1", "PLCK 2"];

  function AddPLCK(index: number) {
    return (
        <div className="p-fluid">
        {AddCombobox("CLK_PCK" + index + "_CSS", "tab_PCKx_combo_css", props.parentUpdate)}
        {AddInputNumber("CLK_PCK" + index + "_PRES", "tab_PCKx_spinner_pres", props.parentUpdate)}
        {AddCheckBox("CLK_SCER_PCK" + index, "tab_PCKx_checkBox_en", props.parentUpdate)}

        {AddDivioType(
          "tab_label_pckxPresValue",
          GetSymbolValue(component_id, "CLK_PCK" + index + "_PRES")
        )}

        {AddBoldLabel(
          "tab_label_MD_SCLK",
          "MD_CLK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "MD_SLOW_CLK")
        )}
        {AddBoldLabel(
          "tab_label_TD_SCLK",
          "TD_SLCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "TD_SLOW_CLOCK")
        )}
        {AddBoldLabel(
          "tab_label_MAINCK",
          "MAINCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "MAINCK")
        )}
        {AddBoldLabel(
          "tab_label_MCK0",
          "MCK0",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "MCK0")
        )}
        {AddBoldLabel(
          "tab_label_PLLACK1",
          "PLLACK1",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "PLLACK1")
        )}
        {AddBoldLabel(
          "tab_label_PLLBCK",
          "PLLBCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "PLLBCK")
        )}
        {AddBoldLabel(
          "tab_label_PLLCCK",
          "PLLCCK",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "PLLCCK")
        )}
        {AddBoldLabel(
          "tab_label_PLLCSRC",
          "PLLCSRC",
          CheckSelectedSymbolValue("CLK_PCK" + index + "_CSS", "PLLCSRC")
        )}
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
        style={GetStyle("button_pckxClockTab")}
        onChange={(e) => setValue(e.value)}
      />
      {!value && NullSelected()}
      {value === "PLCK 0" && AddPLCK(0)}
      {value === "PLCK 1" && AddPLCK(1)}
      {value === "PLCK 2" && AddPLCK(2)}
    </div>
  );
};

export default ProgrammableClockController;
