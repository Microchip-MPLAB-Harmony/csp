import React, { useContext, useEffect, useState } from "react";
import {
  ConfigSymbol,
  PluginConfigContext,
  createClassResolver,
  symbolUtilApi,
  useSymbols,
} from "@mplab_harmony/harmony-plugin-client-lib";
import style from "./channelConfigSummary.module.css";
import { Fieldset } from "primereact/fieldset";
import useSymbolControl from "../channelConfig/useSymbolControl";
import { SymbolIds } from "../channelConfig/ChannelConfigurationTable";
import TriggerSourceComponent from "./channelConfigComponents/TriggerSourceComponent";
import DifferentialComponent from "./channelConfigComponents/DifferentialComponent";
import InputScanComponent from "./channelConfigComponents/InputScanComponent";
import SignedModeComponent from "./channelConfigComponents/SignedModeComponent";
import InterruptComponent from "./channelConfigComponents/InterruptComponent";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
const cx = createClassResolver(style);
const getSignedModeSymbolId = (
  analogInput: string,
  NUM_SIGNALS_COUNT: number
) => {
  const index = analogInput.replace(/[^0-9]/g, "");
  if (parseInt(index) < 16) {
    return `ADCIMCON1__SIGN${index}`;
  }
  if (parseInt(index) >= 16 && parseInt(index) < 32) {
    return `ADCIMCON2__SIGN${index}`;
  }
  if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
    return `ADCIMCON3__SIGN${index}`;
  }
};
const getDiffModeSymbolId = (
  analogInput: string,
  NUM_SIGNALS_COUNT: number
) => {
  const index = analogInput.replace(/[^0-9]/g, "");
  if (parseInt(index) < 16) {
    return `ADCIMCON1__DIFF${index}`;
  }
  if (parseInt(index) >= 16 && parseInt(index) < 32) {
    return `ADCIMCON2__DIFF${index}`;
  }
  if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
    return `ADCIMCON3__DIFF${index}`;
  }
};

const getInterruptSymbolId = (
  analogInput: string,
  NUM_SIGNALS_COUNT: number
) => {
  const index = analogInput.replace(/[^0-9]/g, "");
  if (parseInt(index) < 32) {
    return `ADCGIRQEN1__AGIEN${index}`;
  }
  if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
    return `ADCGIRQEN2__AGIEN${index}`;
  }
};
const getScanInputSymbolId = (
  analogInput: string,
  NUM_SIGNALS_COUNT: number
) => {
  const index = analogInput.replace(/[^0-9]/g, "");
  if (parseInt(index) < 32) {
    return `ADCCSS1__CSS${index}`;
  }
  if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
    return `ADCCSS2__CSS${index}`;
  }
};

const getTriggerSymbolId = (analogInput: string, NUM_SIGNALS_COUNT: number) => {
  const index = analogInput.replace(/[^0-9]/g, "");
  if (parseInt(index) < 4) {
    return `ADCTRG1__TRGSRC${index}`;
  }
  if (parseInt(index) >= 4 && parseInt(index) < 8) {
    return `ADCTRG2__TRGSRC${index}`;
  }
  if (parseInt(index) >= 8 && parseInt(index) < 12) {
    return `ADCTRG3__TRGSRC${index}`;
  }
  if (parseInt(index) >= 12 && parseInt(index) < 16) {
    return `ADCTRG4__TRGSRC${index}`;
  }
  if (parseInt(index) >= 16 && parseInt(index) < 20) {
    return `ADCTRG5__TRGSRC${index}`;
  }
  if (parseInt(index) >= 20 && parseInt(index) < 24) {
    return `ADCTRG6__TRGSRC${index}`;
  }
  if (parseInt(index) >= 24 && parseInt(index) < NUM_SIGNALS_COUNT) {
    return `ADCTRG7__TRGSRC${index}`;
  }
};
const ChannelConfigSummary = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { class2andClass3Menu, NUM_SIGNALS_COUNT } = useSymbolControl();
  const [enabledChannel, setEnabledChannel] = useState<string[]>([]);
  const [symbolIds, setSymbolIds] = useState<SymbolIds[]>([]);

  useEffect(() => {
    symbolUtilApi.getSymbols(componentId, class2andClass3Menu).then((e) => {
      const enable: string[] = [];
      e.map((enabled) => {
        if (enabled.value) {
          enable.push(enabled.symbolId);
        }
      });
      setEnabledChannel(enable);
    });
  }, [class2andClass3Menu]);
  useEffect(() => {
    const symbolIds: SymbolIds[] = [];
    enabledChannel.map((analogInput: string, index) =>
      symbolIds.push({
        analogInput: analogInput,
        enable: analogInput,
        signedMode: getSignedModeSymbolId(analogInput, NUM_SIGNALS_COUNT) || "",
        diffMode: getDiffModeSymbolId(analogInput, NUM_SIGNALS_COUNT) || "",
        interrupt: getInterruptSymbolId(analogInput, NUM_SIGNALS_COUNT) || "",
        inputScan: getScanInputSymbolId(analogInput, NUM_SIGNALS_COUNT) || "",
        triggerSource: getTriggerSymbolId(analogInput, NUM_SIGNALS_COUNT) || "",
        index: index,
      })
    );
    setSymbolIds(symbolIds);
  }, [enabledChannel]);
  return (
    <DataTable value={symbolIds} tableStyle={{ minWidth: "50rem" }}>
      <Column
        field="analogInput"
        header="Analog Input"
        body={(e) => (
          <div style={{ textAlign: "center" }}>{e?.analogInput}</div>
        )}
      ></Column>
      <Column
        field="signedMode"
        header="SignedMode"
        body={(e) => <SignedModeComponent symbolId={e.signedMode} />}
      ></Column>
      <Column
        field="diffMode"
        header="Differential Mode"
        body={(e) => <DifferentialComponent symbolId={e.diffMode} />}
      ></Column>
      <Column
        field="triggerSource"
        header="Trigger Source"
        body={(e) => <TriggerSourceComponent symbolId={e.triggerSource} />}
      ></Column>
      <Column
        field="inputScan"
        header="Input Scan"
        body={(e) => <InputScanComponent symbolId={e.inputScan} />}
      ></Column>

      <Column
        field="interrupt"
        header="Interrupt"
        body={(e) => <InterruptComponent symbolId={e.interrupt} />}
      ></Column>
    </DataTable>
  );
};

export default React.memo(ChannelConfigSummary);
