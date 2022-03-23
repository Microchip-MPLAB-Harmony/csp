import React, { useState } from "react";
import { ListBox } from "primereact/listbox";
import { GetStyle } from "../../../Common/UIComponent";
import { component_id } from "../MainBlock";
import { GetSymbolValue } from "../../../Common/SymbolAccess";
import { AddDummyCheckBox } from "../../../Common/ClockCommonUtils";
import {
  AddColoredFrequencyLabelWithTooltip,
  AddDummyInputNumber,
  AddLabel,
} from "../../../Common/ClockCommonUtils";
import {
  AddCheckBox,
  AddCombobox,
  AddDivioType,
  AddFrequencyLabel,
  AddInputNumber,
} from "../../../Common/ClockCommonUtils";

const PLLController = (props: { parentUpdate: () => void }) => {
  const [value, setValue] = useState("PLL A");
  const tabs = ["PLL A", "PLL B", "PLL C"];

  function AddPLL(letter: string) {
    try {
      const minCoreClockValue = GetSymbolValue(
        component_id,
        "PLL" + letter + "_MINCORECLK_FREQUENCY"
      );
      const maxCoreClockValue = GetSymbolValue(
        component_id,
        "PLL" + letter + "_MAXCORECLK_FREQUENCY"
      );
      const currentCoreClockValue = GetSymbolValue(
        component_id,
        "PLL" + letter + "_CORECLK_FREQUENCY"
      );
      let coreClockFreqstatus =
        Number(currentCoreClockValue) >= Number(minCoreClockValue) &&
        Number(currentCoreClockValue) <= Number(maxCoreClockValue)
          ? true
          : false;
      return (
        <div className="p-fluid">
          {AddCombobox(
            "CLK_PLL" + letter + "_PLLMS",
            "tab_PLLA_combo_source",
            props.parentUpdate
          )}
          {AddInputNumber(
            "CLK_PLL" + letter + "_MUL",
            "tab_PLLA_spinner_mul",
            props.parentUpdate
          )}
          {AddLabel(
            "tab_label_mulValue",
            GetSymbolValue(component_id, "CLK_PLL" + letter + "_MUL")
          )}
          {AddInputNumber(
            "CLK_PLL" + letter + "_FRACR",
            "tab_PLLA_spinner_fracr",
            props.parentUpdate
          )}
          {AddLabel(
            "tab_label_fracrValue",
            GetSymbolValue(component_id, "CLK_PLL" + letter + "_FRACR")
          )}
          {AddInputNumber(
            "CLK_PLL" + letter + "_STEP",
            "tab_PLLA_spinner_step",
            props.parentUpdate
          )}
          {AddInputNumber(
            "CLK_PLL" + letter + "_NSTEP",
            "tab_PLLA_spinner_nstep",
            props.parentUpdate
          )}
          {AddInputNumber(
            "CLK_PLL" + letter + "_DIVPMC0",
            "tab_PLLA_spinner_divpmc0",
            props.parentUpdate
          )}

          {AddCheckBox(
            "CLK_PLL" + letter + "_ENPLL",
            "tab_PLLA_checkBox_enable",
            props.parentUpdate
          )}
          {AddCheckBox(
            "CLK_PLL" + letter + "_ENSPREAD",
            "tab_PLLA_checkBox_enspread",
            props.parentUpdate
          )}
          {AddCheckBox(
            "CLK_PLL" + letter + "_ENPLLO0",
            "tab_PLLA_checkBox_enpllo0",
            props.parentUpdate
          )}

          {AddFrequencyLabel(
            "PLL" + letter + "_REFCLK_FREQUENCY",
            "tab_label_PLLA_refclockFreq"
          )}

          {AddColoredFrequencyLabelWithTooltip(
            "PLL" + letter + "_CORECLK_FREQUENCY",
            "tab_label_PLLA_coRefFrequency",
            coreClockFreqstatus,
            "The core PLL" +
              letter +
              " clock frequency value should be between " +
              minCoreClockValue +
              " and " +
              maxCoreClockValue +
              " Hz."
          )}

          {AddDivioType(
            "tab_PLLA_label_PLLDivPmc0",
            GetSymbolValue(component_id, "CLK_PLL" + letter + "_DIVPMC0")
          )}

          {letter === "A" && PLLAUnique(letter)}
          {(letter === "B" || letter === "C") && CommonPLLBandPLLC(letter)}
        </div>
      );
    } catch (err) {
      alert(err);
    }
  }

  function PLLAUnique(letter: string) {
    return (
      <div>
        {AddInputNumber(
          "CLK_PLL" + letter + "_DIVPMC1",
          "tab_PLLA_spinner_divpmc1",
          props.parentUpdate
        )}
        {AddCheckBox(
          "CLK_PLL" + letter + "_ENPLLO1",
          "tab_PLLA_checkBox_enpllo1",
          props.parentUpdate
        )}
        {AddDivioType(
          "tab_label_PLLA_PLLDivpmc1",
          GetSymbolValue(component_id, "CLK_PLL" + letter + "_DIVPMC1")
        )}
      </div>
    );
  }
  function CommonPLLBandPLLC(letter: string) {
    return (
      <div>
        {AddDummyInputNumber("tab_PLLA_spinner_divpmc1")}
        {AddDummyCheckBox("tab_PLLA_checkBox_enpllo1")}
        {AddLabel("tab_label_PLLA_PLLDivpmc1", "NA")}
      </div>
    );
  }

  function NullSelected() {
    setValue("PLL A");
    return <div>{AddPLL("A")}</div>;
  }

  return (
    <div className="card">
      <ListBox
        value={value}
        options={tabs}
        style={GetStyle("button_PLLx")}
        onChange={(e) => setValue(e.value)}
      />
      {!value && NullSelected()}
      {value === "PLL A" && AddPLL("A")}
      {value === "PLL B" && AddPLL("B")}
      {value === "PLL C" && AddPLL("C")}
    </div>
  );
};

export default PLLController;
