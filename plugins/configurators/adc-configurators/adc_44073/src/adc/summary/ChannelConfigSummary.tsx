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
import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
const cx = createClassResolver(style);
export type ChannelConfigArray = {
  channel: string;
  enable: any;
  signalName: any;
  positiveInput: any;
  negativeInput: any;
  interrupt: any;
  gain: any;
  offset: any;
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
  const [gainSymbols, setGainSymbols] = useState<any>();
  const [offsetSymbols, setOffsetSymbols] = useState<any>();
  const { channelIdObject, MAX_CH_COUNT, productFamily } = useChannelCount();

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
      symbolUtilApi.getSymbols(componentId, channelIdObject.gain),
      symbolUtilApi.getSymbols(componentId, channelIdObject.offset),
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
        setGainSymbols(data[5]);
        setOffsetSymbols(data[6]);
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
        gain: gainSymbols[i],
        offset: offsetSymbols[i],
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
        field="sequenceNumber"
        header="Sequence Number"
        body={(e) => <div style={{ textAlign: "center" }}>{e?.channel}</div>}
      ></Column>
      <Column
        field="signalName"
        header="Signal Name"
        body={(e) => (
          <div style={{ textAlign: "center" }}>{e?.signalName?.value}</div>
        )}
      ></Column>
      <Column
        field="positiveInput"
        header="Positive Input"
        body={(e) => (
          <div style={{ textAlign: "center" }}>{e?.positiveInput?.value}</div>
        )}
      ></Column>
      <Column
        field="negativeInput"
        header="Negative Input"
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
              <i
                className="pi pi-check"
                style={{ color: "green", fontSize: "1.25rem" }}
              ></i>
            ) : (
              <i
                className="pi pi-ban"
                style={{ color :"orange", fontSize: "1.25rem" }}
              ></i>
            )}
          </div>
        )}
      ></Column>
      {productFamily === "SAMRH" && (
        <Column
          field="gain"
          header="Gain"
          body={(e) => (
            <div style={{ textAlign: "center" }}>
              {e?.gain?.selectedOptionPair?.description}
            </div>
          )}
        ></Column>
      )}
      {productFamily === "SAMRH" && (
        <Column
          field="offset"
          header="Offset"
          body={(e) => (
            <div style={{ textAlign: "center" }}>
              {e?.offset?.value ? (
                <i
                  className="pi pi-check"
                  style={{ color: "green", fontSize: "1.25rem" }}
                ></i>
              ) : (
                <i
                  className="pi pi-ban"
                  style={{ color :"orange", fontSize: "1.25rem" }}
                ></i>
              )}
            </div>
          )}
        ></Column>
      )}
    </DataTable>
  );
};

export default React.memo(ChannelConfigSummary);
