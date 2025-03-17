import CLOCKSAMA7D6 from "../Resources/data/react_SAML21.svg";
import positions from "../Resources/data/positions.module.css";
import styles from "./block-diagram-view.module.css";
import tabCss from "../Styles/tab.module.css";
import ClockJson from "../Resources/data/controls.json";
import { useContext, useEffect, useState } from "react";
import ControlInterfac from "clock-common/lib/Tools/ControlInterface";
import { ReactComponent as ADCBlockDiagram } from "../Resources/data/react_SAML21.svg";
import {
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { MenuItem } from "primereact/menuitem";
import { ConfirmDialog } from "primereact/confirmdialog";
import Gclk0Controller from "./ClockBox/GCLK/Gclk0ControllerBox";
import Gclk1Controller from "./ClockBox/GCLK/Gclk1ControllerBox";
import GclkXControllerBox from "./ClockBox/GCLK/GclkXControllerBox";
import MainClockControllerBox from "./ClockBox/MainClockControllerBox";
import PeripheralClockControllerBox from "./ClockBox/PopUp/PeripheralClockControllerBox";
import RTCClockControllerBox from "./ClockBox/RTCClockControllerBox";
import InternalOscillatorConfig from "./ClockBox/InternalOscillatorConfig";
import DFLLControllerBox from "./ClockBox/DFLLControllerBox";
import FDPLLControllerBox from "./ClockBox/FDPLLControllerBox";
import Crstal32KhzOscialltorControllerBox from "./ClockBox/Crstal32KhzOscialltorControllerBox";
import { initializeSVG } from "../SVGhandler";

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
  useEffect(() => {
    initializeSVG(componentId, cx);
  }, []);
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
          {/* <img
            src={CLOCKSAMA7D6}
            alt='icon'
            className={cx('main-block-diagram')}
          /> */}
          <ADCBlockDiagram id="clk_sam_l21-main-image"></ADCBlockDiagram>
           <InternalOscillatorConfig
            clockController={getBoxControlData('')}
            cx={cx}
          />
          <DFLLControllerBox
            clockController={getBoxControlData('dfllBox')}
            cx={cx}
          />
          <FDPLLControllerBox
          clockController={getBoxControlData('')}
          cx={cx}
        />
        <Crstal32KhzOscialltorControllerBox
            clockController={getBoxControlData('32khzOScillatorBox')}
            cx={cx}
          />
          <Gclk0Controller
            gclk0Controller={getBoxControlData('gclkGen0SourceBox')}
            cx={cx}
          />
          <Gclk1Controller
            gclk1Controller={getBoxControlData('gclkGen1SourceBox')}
            cx={cx}
          />
          <GclkXControllerBox
            controller={getBoxControlData('gclkGenXSourceBox')}
            cx={cx}
          />
          <MainClockControllerBox
            clockController={getBoxControlData('mainClkBox')}
            cx={cx}
          />
          <PeripheralClockControllerBox
            clockController={getBoxControlData('peripheralClkBox')}
            cx={cx}
          />
          <RTCClockControllerBox
            clockController={getBoxControlData('rtcClkBox')}
            cx={cx}
          />
        </div>
      </div>
    </>
  );
};
export default MainBlock;
