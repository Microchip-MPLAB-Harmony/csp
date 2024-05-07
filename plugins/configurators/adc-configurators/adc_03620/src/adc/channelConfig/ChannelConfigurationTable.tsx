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
type Props = {
  moduleId: number;
};
export type SymbolIds = {
  index: number;
  enableSigneData: string;
  enable: string;
  channelInScan: string;
  mode: string;
  triggerSource: string;
  enableInterrupt: string;
};
const ChannelConfigurationTable = ({ moduleId }: Props) => {
  const { symbolIds } = useSymbolControl(moduleId);

  return (
    <DataTable value={symbolIds} tableStyle={{ minWidth: "10rem" }}>
      <Column
        field="channel"
        header="Channel"
        body={(e) => AnalogInputComponent(e)}
      ></Column>
      <Column
        field="enable"
        header="Enable"
        body={(e) => EnableComponent(e)}
      ></Column>

      <Column
        field="signedMode"
        header="Enable Signed Data"
        body={(e) => SignedModeComponent(e)}
      ></Column>

      <Column
        field="inputScan"
        header="Include Channel in Scan"
        body={(e) => InputScanComponent(e)}
      ></Column>
      <Column
        field="diffMode"
        header="Mode"
        body={(e) => DifferentialComponent(e)}
      ></Column>
      <Column
        field="triggerSource"
        header="Trigger Source"
        body={(e) => TriggerSourceComponent(e)}
      ></Column>
      <Column
        field="interrupt"
        header="Enable Channel Ready Interrupt"
        body={(e) => InterruptComponent(e)}
      ></Column>
    </DataTable>
  );
};

export default React.memo(ChannelConfigurationTable);
