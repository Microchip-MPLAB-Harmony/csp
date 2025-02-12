import CLOCKSAMA7D6 from "../Resources/data/react_SAM9X60.svg";
import positions from "../Resources/data/positions.module.css";
import styles from "./block-diagram-view.module.css";
import tabCss from "../Styles/tab.module.css";
import ClockJson from "../Resources/data/controls.json";
import { useContext, useEffect, useState } from "react";
import ControlInterfac from "clock-common/lib/Tools/ControlInterface";
import {
  CheckBoxDefault,
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { MenuItem } from "primereact/menuitem";
import { ConfirmDialog } from "primereact/confirmdialog";
import SlowClockController from "./ClockBox/SlowClockController";
import MainClockController from "./ClockBox/MainClockController";
import PLLAClockController from "./ClockBox/PLLAController";
import UPLLClockController from "./ClockBox/UPLLClockController";
import PClockController from "./ClockBox/PClockController";
import GclkXControllerBox from "./ClockBox/GCLK/GclkXControllerBox";
import USBClockController from "./ClockBox/USBClockController";
import PeripheralClockControllerBox from "./ClockBox/PopUp/PeripheralClockControllerBox";
import GenericClockConfigBox from "./ClockBox/PopUp/GenericClockConfigBox";

export let controlJsonData = ClockJson as ControlInterfac[];
export function getBoxControlData(boxId: string) {
  return controlJsonData.filter((e) => e.box_id === boxId);
}

const cx = createClassResolver(positions, styles, tabCss);

const MainBlock = () => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const zoomableContainer = useZoomableContainer();
  const pannableContainer = usePannableContainer();

  useEffect(() => {}, []);

  const items: MenuItem[] = [
    {
      label: "Zoom",
      icon: "pi pi-search-plus",
      items: [
        {
          label: "Zoom In (Alt + Scroll Up)",
          icon: "pi pi-fw pi-search-plus",
          command: () => zoomableContainer.zoomIn(),
        },
        {
          label: "Reset Zoom (Alt + Scroll Click)",
          icon: "pi pi-fw pi-refresh",
          command: () => zoomableContainer.resetZoom(),
        },
        {
          label: "Zoom Out (Alt + Scroll Down)",
          icon: "pi pi-fw pi-search-minus",
          command: () => zoomableContainer.zoomOut(),
        },
      ],
    },
  ];

  return (
    <>
      <ConfirmDialog />
      <PluginToolbar menuItems={items} title="Clock Configurator" />
      <div
        className={cx("pannable-container")}
        ref={pannableContainer.ref}
        {...pannableContainer.props}
      >
        <div
          className={cx("svg-container")}
          ref={zoomableContainer.ref}
          {...zoomableContainer.props}
        >
          <img
            src={CLOCKSAMA7D6}
            alt="icon"
            className={cx("main-block-diagram")}
          />
          <CheckBoxDefault  componentId={componentId} symbolId="CLK_GENERATOR_CODE" className={cx('clk_code_generator_en')} />
          <label className={cx('generatorLabel')}> Enable Generator Initialization</label>
          <SlowClockController
            clockController={getBoxControlData('')}
            cx={cx}
          />
          <MainClockController
            clockController={getBoxControlData('')}
            cx={cx}
          />
          <PLLAClockController clockController={getBoxControlData('')}
            cx={cx}
          />
          <UPLLClockController clockController={getBoxControlData('')}
            cx={cx}
          />
          <PClockController clockController={getBoxControlData('')}
            cx={cx}
          />
          <GclkXControllerBox controller={[]}
            cx={cx}
          />
          <USBClockController clockController={[]}
            cx={cx}
          />
          <PeripheralClockControllerBox clockController={[]} cx={cx}/>
          <GenericClockConfigBox clockController={[]} cx={cx}/>
          
          
        </div>
      </div>
    </>
  );
};
export default MainBlock;
