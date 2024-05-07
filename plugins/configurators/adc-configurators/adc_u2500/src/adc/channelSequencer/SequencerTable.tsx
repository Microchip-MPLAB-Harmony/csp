import React, { useContext } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import {
  PluginConfigContext,
  createClassResolver,
  CheckBoxDefault,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import style from "./channelSequencer.module.css";
import useChannelSequencerSymbols from "./useChannelSequencerSymbols";
const cx = createClassResolver(style);

const SequencerTable = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { symbolIds } = useChannelSequencerSymbols();
  const Labels = (symbolId: string) => {
    const symbol = useBooleanSymbol({ componentId, symbolId });
    return <div>{symbol.label.replace("", "")}</div>;
  };
  const DefaultDropDown = (symbol: string) => {
    return (
      <CheckBoxDefault
        hidden={false}
        componentId={componentId}
        symbolId={symbol}
        className={cx("defaultControl")}
      ></CheckBoxDefault>
    );
  };

  return (
    <DataTable value={symbolIds} tableStyle={{ minWidth: "30rem" }}>
      <Column
        field="register"
        header="Register"
        body={Labels}
      ></Column>
      <Column field="enable" header="Enable" body={DefaultDropDown}></Column>
    </DataTable>
  );
};

export default React.memo(SequencerTable);
