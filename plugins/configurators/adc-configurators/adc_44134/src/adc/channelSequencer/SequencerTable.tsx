import React, { useContext } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import {
  PluginConfigContext,
  createClassResolver,
  ComboBoxDefault,
  useComboSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import style from "./channelSequencer.module.css";
import useChannelSequencerSymbols from "./useChannelSequencerSymbols";
const cx = createClassResolver(style);

const SequencerTable = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { symbolIds } = useChannelSequencerSymbols();
  const Labels = (symbolId: string) => {
    const symbol = useComboSymbol({ componentId, symbolId });
    return <div>{symbol.label.replace("Select Channel for", "")}</div>;
  };
  const DefaultDropDown = (symbol: string) => {
    return (
      <ComboBoxDefault
        componentId={componentId}
        symbolId={symbol}
        hidden={false}
        className={cx("defaultControl")}
      ></ComboBoxDefault>
    );
  };

  return (
    <DataTable value={symbolIds} tableStyle={{ minWidth: "30rem" }}>
      <Column
        field="sequenceNumber"
        header="Sequence Number"
        body={Labels}
      ></Column>
      <Column field="channel" header="Channel" body={DefaultDropDown}></Column>
    </DataTable>
  );
};

export default React.memo(SequencerTable);
