import React from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import useSymbolControl from "./useSymbolControl";
import AnalogInputComponent from "./AnalogInputComponent";
import EnableComponent from "./EnableComponent";
import DifferentialComponent from "./DifferentialComponent";
import InputScanComponent from "./InputScanComponent";
import InterruptComponent from "./InterruptComponent";
import SignedModeComponent from "./SignedModeComponent";
import TriggerSourceComponent from "./TriggerSourceComponent";

export type SymbolIds = {
  index: number;
  analogInput: string;
  enable: string;
  signedMode: string;
  diffMode: string;
  triggerSource: string;
  inputScan: string;
  interrupt: string;
};
const ChannelConfigurationTable: React.FunctionComponent = () => {
  const { symbolIds } = useSymbolControl();

  return (
    <DataTable value={symbolIds} tableStyle={{ minWidth: "50rem" }}>
      <Column
        field="analogInput"
        header="Analog Input"
        body={(e) => AnalogInputComponent(e)}
      ></Column>
      <Column
        field="enable"
        header="Enable"
        body={(e) => EnableComponent(e)}
      ></Column>
      <Column
        field="signedMode"
        header="SignedMode"
        body={(e) => SignedModeComponent(e)}
      ></Column>
      <Column
        field="diffMode"
        header="Differential Mode"
        body={(e) => DifferentialComponent(e)}
      ></Column>
      <Column
        field="triggerSource"
        header="Trigger Source"
        body={(e) => TriggerSourceComponent(e)}
      ></Column>
      <Column
        field="inputScan"
        header="Input Scan"
        body={(e) => InputScanComponent(e)}
      ></Column>

      <Column
        field="interrupt"
        header="Interrupt"
        body={(e) => InterruptComponent(e)}
      ></Column>
    </DataTable>
  );
};

export default React.memo(ChannelConfigurationTable);
