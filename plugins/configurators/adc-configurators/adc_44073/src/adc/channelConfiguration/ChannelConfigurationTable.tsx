import React from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import SequenceNumber from "./SequenceNumber";
import EnableComponent from "./EnableComponent";
import InterruptComponent from "./InterruptComponent";
import NegativeInputComponent from "./NegativeInputComponent";
import SignalNameComponent from "./SignalNameComponent";
import PositiveInputComponent from "./PositiveInputComponent";
import useChannelCount from "./useChannelCount";
import GainComponent from "./GainComponent";
import OffsetComponet from "./OffsetComponent";
export type ChannelIds = {
  index: number;
  channel: string;
  enable: string;
  signalName: string;
  positiveInput: string;
  negativeInput: string;
  interrupt: string;
  gain: string;
  offset: string;
};
const ChannelConfigurationTable: React.FunctionComponent = () => {
  const { channelIds, MAX_CH_COUNT, productFamily } = useChannelCount();

  return (
    <DataTable value={channelIds} tableStyle={{ minWidth: "50rem" }}>
      <Column
        field="sequenceNumber"
        header="Sequence Number"
        body={(e) => SequenceNumber(e, MAX_CH_COUNT)}
      ></Column>
      <Column
        field="enable"
        header="Enable"
        body={(e) => EnableComponent(e, MAX_CH_COUNT)}
      ></Column>
      <Column
        field="signalName"
        header="Signal Name"
        body={(e) => SignalNameComponent(e, MAX_CH_COUNT)}
      ></Column>
      <Column
        field="positiveInput"
        header="Positive Input"
        body={(e) => PositiveInputComponent(e, MAX_CH_COUNT)}
      ></Column>
      <Column
        field="negativeInput"
        header="Negative Input"
        body={(e) => NegativeInputComponent(e, MAX_CH_COUNT)}
      ></Column>
      <Column
        field="interrupt"
        header="Interrupt"
        body={(e) => InterruptComponent(e, MAX_CH_COUNT)}
      ></Column>
      {productFamily === "SAMRH" && (
        <Column
          field="gain"
          header="Gain"
          body={(e) => GainComponent(e, MAX_CH_COUNT)}
        ></Column>
      )}
      {productFamily === "SAMRH" && (
        <Column
          field="offset"
          header="Offset"
          body={(e) => OffsetComponet(e, MAX_CH_COUNT)}
        ></Column>
      )}
    </DataTable>
  );
};

export default React.memo(ChannelConfigurationTable);
