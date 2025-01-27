import CLOCKSAMA7D6 from "../Resources/data/react_SAMRH71.svg";
import positions from "../Resources/data/positions.module.css";
import styles from "./block-diagram-view.module.css";
import tabCss from "../Styles/tab.module.css";
import ClockJson from "../Resources/data/controls.json";
import { useContext, useEffect, useState } from "react";
import ControlInterfac from "clock-common/lib/Tools/ControlInterface";
import {
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { MenuItem } from "primereact/menuitem";
import { ConfirmDialog } from "primereact/confirmdialog";
import MDSLClockBox from "./ClockBox/MDSLClockBox";
import MainClockController from "./ClockBox/MainClockController";
import PLLAClockController from "./ClockBox/PLLAClockController";
import PLLBClockController from "./ClockBox/PLLBClockController";
import MasterClockBox from "./ClockBox/MasterClockCOntroller";
import GclkXControllerBox from "./ClockBox/GCLK/GclkXControllerBox";
import PeripheralClockControllerBox from "./ClockBox/PopUp/PeripheralClockControllerBox";
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
          <MDSLClockBox
            clockController={getBoxControlData("mdslClockBox")}
            cx={cx}
          />
          <MainClockController
            clockController={getBoxControlData("mainClockBox")}
            cx={cx}
          />
          <PLLAClockController
            clockController={getBoxControlData("PLLAClockBox")}
            cx={cx}
          />
          <PLLBClockController
            clockController={getBoxControlData("PLLBClockBox")}
            cx={cx}
          />
          <MasterClockBox clockController={getBoxControlData("MasterClockBox")}
            cx={cx}
          />
          <GclkXControllerBox cx={cx} controller={getBoxControlData('gclkGenXSourceBox')}/>
          <PeripheralClockControllerBox
            clockController={getBoxControlData('')}
            cx={cx}
          />

        </div>
      </div>
    </>
  );
};
export default MainBlock;
