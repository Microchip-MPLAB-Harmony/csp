import { useContext, useEffect, useRef, useState } from "react";
import { ReactComponent as ADCBlockDiagram } from "../images/react_adc_44073.svg";
import { OverlayPanel } from "primereact/overlaypanel";
import styles from "./BlockDiagramView.module.css";
import positions from "../styles/positions.module.css";
import short_names_adc_gallardo from "../resources/short_names_adc_gallardo.json";
import short_names_adc_mistral from "../resources/short_names_adc_mistral.json";
import {
  usePannableContainer,
  useZoomableContainer,
  useScreehshot,
  PluginToolbar,
  PluginConfigContext,
  createClassResolver,
  shortNamesApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { initializeSVG } from "./SVGhandler";
import WindowComparison from "./windowComparison/WindowComparison";
import TriggerSymbols from "./trigger/TriggerSymbols";
import GeneralConfiguration from "./generalConfiguration/GeneralConfiguration";
import ChannelSequencer from "./channelSequencer/ChannelSequencer";
import ChannelConfiguration from "./channelConfiguration/ChannelConfiguration";
import Summary from "./summary/Summary";
import { Dialog } from "primereact/dialog";
import useChannelCount from "./channelConfiguration/useChannelCount";

const cx = createClassResolver(positions, styles);
function BlockDiagramView() {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [summaryPopup, setSummaryPopup] = useState(false);
  const pannableContainer = usePannableContainer();
  const zoomableContainer = useZoomableContainer();
  const screenShotHook = useScreehshot();
  const { productFamily } = useChannelCount();
  const op = useRef<OverlayPanel>(null);

  useEffect(() => {
    screenShotHook.ref.current = zoomableContainer.ref.current;
  }, [zoomableContainer.ref]);
  useEffect(() => {
    if (productFamily === "SAMRH") {
      shortNamesApi.applyShortNames(
        componentId,
        "ADC_MENU",
        short_names_adc_mistral
      );
    }

    initializeSVG(componentId, cx);
  }, [componentId, productFamily]);

  const items = [
    {
      label: "Summary",
      icon: "pi pi-fw pi-chart-bar",
      expanded: true,
      command: () => {
        setSummaryPopup(true);
      },
    },
    {
      label: "Zoom",
      icon: "pi pi-search-plus",
      command: (e: any) => op.current?.toggle(e),
      items: [
        {
          label: "Zoom In (Alt + Scroll Up)",
          icon: "pi pi-fw pi-search-plus",
          command: () => {
            zoomableContainer.zoomIn();
          },
        },
        {
          label: "Reset Zoom (Alt + Scroll Click)",
          icon: "pi pi-fw pi-refresh",
          command: () => {
            zoomableContainer.resetZoom();
          },
        },
        {
          label: "Zoom Out (Alt + Scroll Down)",
          icon: "pi pi-fw pi-search-minus",
          command: () => {
            zoomableContainer.zoomOut();
          },
        },
      ],
    },
  ];

  return (
    <div>
      <PluginToolbar menuItems={items} title={"ADC Configurator"} />
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
          <div>
            <ADCBlockDiagram id="adc_44073-main-image"></ADCBlockDiagram>
            <TriggerSymbols />
            <WindowComparison />
            <GeneralConfiguration />
            <ChannelSequencer />
            <ChannelConfiguration />
          </div>
        </div>
      </div>
      <Dialog
        header="ADC Summary"
        visible={summaryPopup}
        maximizable={true}
        onHide={() => {
          setSummaryPopup(!summaryPopup);
        }}
      >
        <Summary />
      </Dialog>
    </div>
  );
}

export default BlockDiagramView;
