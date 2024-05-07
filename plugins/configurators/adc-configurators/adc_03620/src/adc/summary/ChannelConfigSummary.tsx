import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  createClassResolver,
  symbolUtilApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import style from "./channelConfigSummary.module.css";
import { Fieldset } from "primereact/fieldset";
import { SymbolIds } from "../channelConfig/ChannelConfigurationTable";
import TriggerSourceComponent from "./channelConfigComponents/TriggerSourceComponent";
import DifferentialComponent from "./channelConfigComponents/DifferentialComponent";
import InputScanComponent from "./channelConfigComponents/InputScanComponent";
import SignedModeComponent from "./channelConfigComponents/SignedModeComponent";
import InterruptComponent from "./channelConfigComponents/InterruptComponent";
import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
const cx = createClassResolver(style);
type Props = {
  moduleId: number | string;
};
const ChannelConfigSummary = ({ moduleId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [channelList, setChannelList] = useState<string[]>([]);
  const [enabledChannel, setEnabledChannel] = useState<string[]>([]);
  const [symbolIds, setSymbolIds] = useState<SymbolIds[]>([]);

  useEffect(() => {
    symbolUtilApi
      .getChildren(componentId, `ADC_CORE_${moduleId}_CHANNEL_CONFIG`)
      .then((module: string[]) => {
        setChannelList(module);
      });
  }, []);

  useEffect(() => {
    symbolUtilApi.getSymbols(componentId, channelList).then((e) => {
      const enable: string[] = [];
      e.map((enabled) => {
        if (enabled.value) {
          enable.push(enabled.symbolId);
        }
      });
      setEnabledChannel(enable);
    });
  }, [channelList]);
  useEffect(() => {
    const symbolIds: SymbolIds[] = [];
    enabledChannel.map((value: string) => {
      let channelIndex = value.split("_")[4];
      symbolIds.push({
        index: parseInt(channelIndex),
        enable: `ADC_CORE_${moduleId}_CH_${channelIndex}_ENABLE`,
        enableSigneData: `ADC_CORE_${moduleId}_CH_${channelIndex}_CHNCFG3_SIGN`,
        channelInScan: `ADC_CORE_${moduleId}_CH_${channelIndex}_CHNCFG2_CSS`,
        mode: `ADC_CORE_${moduleId}_CH_${channelIndex}_CHNCFG3_DIFF`,
        triggerSource: `ADC_CORE_${moduleId}_CH_${channelIndex}_CHNCFG4_5_TRGSRC`,
        enableInterrupt: `ADC_CORE_${moduleId}_CH_${channelIndex}_INTENSET_CHRDY`,
      });
    });
    setSymbolIds(symbolIds);
  }, [enabledChannel]);
  return (
    <DataTable value={symbolIds} tableStyle={{ minWidth: "50rem" }}>
      <Column
        field="channel"
        header="Channel"
        body={(e) => (
          <div style={{ textAlign: "center" }}>{ e.index}</div>
        )}
      ></Column>
      <Column
        field="enableSigneData"
        header="Enable Signed Data"
        body={(e) => <SignedModeComponent symbolId={e.enableSigneData} />}
      ></Column>
      <Column
        field="channelInScan"
        header="Include Channel in Scan "
        body={(e) => <InputScanComponent symbolId={e.channelInScan} />}
      ></Column>
      <Column
        field="mode"
        header="Mode"
        body={(e) => <DifferentialComponent symbolId={e.mode} />}
      ></Column>
      <Column
        field="triggerSource"
        header="Trigger Source"
        body={(e) => <TriggerSourceComponent symbolId={e.triggerSource} />}
      ></Column>

      <Column
        field="enableInterrupt"
        header="Interrupt"
        body={(e) => <InterruptComponent symbolId={e.enableInterrupt} />}
      ></Column>
    </DataTable>
  );
};

export default ChannelConfigSummary;
