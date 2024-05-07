import React, { useContext, useEffect, useState } from "react";
import {
  ConfigSymbol,
  PluginConfigContext,
  createClassResolver,
  symbolUtilApi,
  useSymbols,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useChannelCount from "../channelConfiguration/useChannelCount";
import style from "./channelConfigSummary.module.css";
import { Fieldset } from "primereact/fieldset";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
const cx = createClassResolver(style);
export type ChannelConfigArray = {
  channel: string;
  enable: any;
  signalName: any;
  positiveInput: any;
  negativeInput: any;
  interrupt: any;
};
const ChannelConfigSummary = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [channelConfigArray, setChannelConfigArray] = useState<
    ChannelConfigArray[]
  >([]);
  const [enableChannelConfigArray, setEnableChannelConfigArray] = useState<
    ChannelConfigArray[]
  >([]);
  const [dummyTrigger, setDummyTrigger] = useState<any>("");
  const [enableSymbols, setEnableSymbols] = useState<any>();
  const [signalNameSymbols, setSignalNameSymbols] = useState<any>();
  const [interruptSymbols, setInterruptSymbols] = useState<any>();
  const [positiveInputSymbols, setPositiveInputSymbols] = useState<any>();
  const [negativeInputSymbols, setNegativeInputSymbols] = useState<any>();
  const { channelIdObject, MAX_CH_COUNT } = useChannelCount();

  useEffect(() => {
    symbolUtilApi
      .getSymbols(componentId, channelIdObject.enable)
      .then((e) => setDummyTrigger(e));
  }, []);

  useEffect(() => {
    const urls = [
      symbolUtilApi.getSymbols(componentId, channelIdObject.enable),
      symbolUtilApi.getSymbols(componentId, channelIdObject.signalName),
      symbolUtilApi.getSymbols(componentId, channelIdObject.interrupt),
      symbolUtilApi.getSymbols(componentId, channelIdObject.positiveInput),
      symbolUtilApi.getSymbols(componentId, channelIdObject.negativeInput),
    ];

    const fetchData = async () => {
      try {
        const responses = await Promise.all(urls.map((url) => url));
        const data = await Promise.all(responses.map((response) => response));
        setEnableSymbols(data[0]);
        setSignalNameSymbols(data[1]);
        setInterruptSymbols(data[2]);
        setPositiveInputSymbols(data[3]);
        setNegativeInputSymbols(data[4]);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [dummyTrigger]);

  useEffect(() => {
    let chanArray = channelIdObject.channel.map((e, i) => {
      return {
        channel: e,
        enable: enableSymbols[i],
        interrupt: interruptSymbols[i],
        signalName: signalNameSymbols[i],
        positiveInput: positiveInputSymbols[i],
        negativeInput: negativeInputSymbols[i],
      };
    });
    setChannelConfigArray(chanArray);
  }, [negativeInputSymbols]);

  useEffect(() => {
    const channelSymbol: ChannelConfigArray[] = [];
    channelConfigArray.map((e, i) => {
      const index = e?.channel?.replace(/^\D+/g, "");
      if (
        parseInt(index) < MAX_CH_COUNT &&
        e?.enable?.value &&
        e?.positiveInput?.value !==
          channelConfigArray[i - 1]?.negativeInput?.value
      ) {
        channelSymbol.push(e);
      }
      if (parseInt(index) > MAX_CH_COUNT && e?.enable?.value) {
        channelSymbol.push(e);
      }
    });
    setEnableChannelConfigArray(channelSymbol);
  }, [channelConfigArray]);

  return (
    <DataTable
      value={enableChannelConfigArray}
      tableStyle={{ minWidth: "50rem" }}
    >
      <Column
        field="Channel"
        header="channel"
        body={(e) => <div style={{ textAlign: "center" }}>{e?.channel}</div>}
      ></Column>
      <Column
        field="signalName"
        header="signal Name"
        body={(e) => (
          <div style={{ textAlign: "center" }}>{e?.signalName?.value}</div>
        )}
      ></Column>
      <Column
        field="positiveInput"
        header="Positive Input"
        body={(e) => (
          <div style={{ textAlign: "center" }}> {e?.positiveInput?.value}</div>
        )}
      ></Column>
      <Column
        field="negativeInput"
        header="negative Input"
        body={(e) => (
          <div style={{ textAlign: "center" }}>{e?.negativeInput?.value}</div>
        )}
      ></Column>

      <Column
        field="interrupt"
        header="Interrupt"
        body={(e) => (
          <div style={{ textAlign: "center" }}>
            {e?.interrupt?.value ? (
              <i className="pi pi-check" style={{ color: "green", fontSize: '1.25rem' }}></i>
            ) : (
              <i className="pi pi-ban" style={{ color: "orange", fontSize: '1.25rem' }}></i>
            )}
          </div>
        )}
      ></Column>
    </DataTable>
  );
};

export default React.memo(ChannelConfigSummary);
