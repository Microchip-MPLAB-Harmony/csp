import { useContext, useState } from "react";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";

import { ListBox } from "primereact/listbox";
import PCKClkControllerBoxTemplate from "./PCKClockControllerBoxTemplate";
import {
  PluginConfigContext,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { getPckClkSettingsSymbol } from "./PCKClockSettingsSymbol";

interface Tab {
  name: string;
  id: string;
  status: string;
}

export const pckTabs: Tab[] = [
  { name: "PLL0", id: "0", status: 'CONFIG_CLOCK_PLL0_ENABLE' },
  { name: "PLL1", id: "1", status: 'CONFIG_CLOCK_PLL1_ENABLE' },
];

const PCKClockControllerXBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(pckTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const pckClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status,
    });
    return (
      <div
        style={{ fontSize: "10px" }}
        className={
          pckClocKEnable.value ? props.cx("enable") : props.cx("disable")
        }
      >
        {option.name}
      </div>
    );
  };
  
  return (
    <div>
      <div>
        <ListBox
          className={props.cx("pllTabbedPane")}
          value={value}
          options={pckTabs}
          optionLabel="name"
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <PCKClkControllerBoxTemplate
        tabTitle={value?.name ? value.id : "0"}
        clkSettingsSymbolArray={getPckClkSettingsSymbol(
          value?.name ? value.name : "PLL0"
        )}
        clkController={props.controller}
        componentId={componentId}
        cx={props.cx}
      />
      <div className={props.cx("userCode")} ><div style={{textAlign:'center'}}>4 MHz &le; <b>Fpfd</b> &le; 60 MHz</div>
      <div style={{textAlign:'center'}}>800 MHz &le; <b>Fvco</b> &le; 1600 MHz</div>
      <div style={{textAlign:'center'}}>12.7 MHz &le; <b>PLLx_y</b> &le; 1600 MHz</div></div>
    </div>
  );
};
export default PCKClockControllerXBox;
