import React, { useContext } from "react";
import {
  PluginConfigContext,
  createClassResolver,
  useSymbols,
  ConfigSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useChannelSequencerSymbols from "../channelSequencer/useChannelSequencerSymbols";
import style from "./channelSequenceSummary.module.css";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";

const cx = createClassResolver(style);
const ChannelSequenceSummary = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { isChannelSequencer, symbolIds } = useChannelSequencerSymbols();
  const symbols = useSymbols({ componentId, symbolIds }) as ConfigSymbol<any>[];
  const enabledSequencer: any = [];
  symbols.map((sequece) => {
    if (sequece?.value !== "NONE") {
      enabledSequencer.push({
        sequenceNumber: sequece?.label?.replace("Select Channel for", ""),
        channel: sequece?.value,
      });
    }
    return 0;
  });
  return (
    <>
      {!isChannelSequencer.value ? (
        <div>Channel Sequencer Disabled</div>
      ) : (
        <DataTable value={enabledSequencer} tableStyle={{ minWidth: "10rem" }}>
          <Column
            field="sequenceNumber"
            header="Sequence Number"
            body={(e) => <div>{e?.sequenceNumber}</div>}
          ></Column>
          <Column
            field="channel"
            header="Channel"
            body={(e) => <div>{e?.channel}</div>}
          ></Column>
        </DataTable>
      )}
    </>
  );
};

export default React.memo(ChannelSequenceSummary);
