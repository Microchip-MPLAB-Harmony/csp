import { ReactComponent as ClockSAME5x } from "../Resources/data/react_SAM_E5x.svg";
import positions from "../Resources/data/positions.module.css";
import styles from "./block-diagram-view.module.css";
import tabCss from "../Styles/tab.module.css";
import ClockSamE5xJson from "../Resources/data/controls.json";
import { useContext, useEffect, useState } from "react";
import { ConfirmDialog } from "primereact/confirmdialog";
import CrytalOscillators48MHzControllerXBox from "./ClockBox/CRYSTALTab/CrytalOscillators48MHzControllerXBox";
import FDPLLControllerXBox from "./ClockBox/FDPLLTab/FDPLLControllerXBox";

import {
  createClassResolver,
  PluginConfigContext,
  PluginToolbar,
  usePannableContainer,
  useZoomableContainer,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { MenuItem } from "primereact/menuitem";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import DFLLController from "./ClockBox/DFLLController";
import Oscillators32KHzControllerBox from "./ClockBox/Oscillators32KHzControllerBox";
import Gclk0ControllerBox from "./ClockBox/GCLK/Gclk0ControllerBox";
import Gclk1ControllerBox from "./ClockBox/GCLK/Gclk1ControllerBox";
import GclkXControllerBox from "./ClockBox/GCLK/GclkXControllerBox";
import { initializeSVG } from "./SVGHandler";
import MainClockController from "./ClockBox/MainClockController";
import PeripheralClockControllerBox from "./ClockBox/PopUp/PeripheralClockControllerBox";
import RTCClockController from "./ClockBox/RTCClockController";
export let component_id = "core";

export let controlJsonData = ClockSamE5xJson as ControlInterface[];

export const cx = createClassResolver(positions, styles, tabCss);
const MainBlock = () => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const [summaryDialogVisible, setSummaryDialogVisible] = useState(false);

  const zoomableContainer = useZoomableContainer();
  const pannableContainer = usePannableContainer();

  // const { height, width } = useWindowDimensions();

  useEffect(() => {
    initializeSVG(cx);
  }, []);
  // useEffect(() => {
  //   console.log(height, width);
  // }, [height, width]);

  function getBoxControlData(boxId: string) {
    return controlJsonData.filter((e) => e.box_id === boxId);
  }

  const items: MenuItem[] = [
    // {
    //   label: 'Summary',
    //   icon: 'pi pi-fw pi-chart-bar',
    //   command: () => setSummaryDialogVisible(true)
    // },
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
  try {
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
            <ClockSAME5x id="clk_sam_e5x-main-image"></ClockSAME5x>
            <CrytalOscillators48MHzControllerXBox
              oscillatorData={getBoxControlData(
                "cry_oscillators_8_48ControllerBox"
              )}
              cx={cx}
            />
            <DFLLController
              dfllControllerData={getBoxControlData("e5x_dfllControllerBox")}
              cx={cx}
            />
            <FDPLLControllerXBox
              fdpllData={getBoxControlData("fdpllControllerBox")}
              cx={cx}
            />
            <Oscillators32KHzControllerBox
              oscillatorData={getBoxControlData("oScillators32KhzController")}
              cx={cx}
            />
            <Gclk0ControllerBox
              gclk0Controller={getBoxControlData("gclkGen0Box")}
              cx={cx}
            />
            <Gclk1ControllerBox
              gclk1Controller={getBoxControlData("gclkGen1Box")}
              cx={cx}
            />
            <GclkXControllerBox
              controller={getBoxControlData("gclkGenXBox")}
              cx={cx}
            />
            <MainClockController
              mainClockController={getBoxControlData("mainClockBox")}
              cx={cx}
            />
            <PeripheralClockControllerBox cx={cx} />
            <RTCClockController
              rtcClockController={getBoxControlData("rtcClockSelBox")}
              cx={cx}
            />
          </div>
        </div>
      </>
    );
  } catch (error) {
    console.log(error);
    return <>Error Occurred! </>;
  }
};
export default MainBlock;
