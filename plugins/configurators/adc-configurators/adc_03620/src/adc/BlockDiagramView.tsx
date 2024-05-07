import { useContext, useEffect, useRef, useState } from "react";
import { ReactComponent as ADCBlockDiagram } from "../images/react_adc_03620.svg";
import { OverlayPanel } from "primereact/overlaypanel";
import styles from "./BlockDiagramView.module.css";
import positions from "../styles/positions.module.css";
import {
  usePannableContainer,
  useZoomableContainer,
  useScreehshot,
  PluginToolbar,
  PluginConfigContext,
  createClassResolver,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { initializeSVG } from "./SVGhandler";                     
import Summary from "./summary/Summary";
import { Dialog } from "primereact/dialog";
import ADCComponentLIst from "./adcComponentList/ADCModule";
const cx = createClassResolver(positions, styles);
function BlockDiagramView() {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [summaryPopup, setSummaryPopup] = useState(false);
  const pannableContainer = usePannableContainer();
  const zoomableContainer = useZoomableContainer();
  const screenShotHook = useScreehshot();
  const op = useRef<OverlayPanel>(null);
  useEffect(() => {
    screenShotHook.ref.current = zoomableContainer.ref.current;
  }, [zoomableContainer.ref]);

  useEffect(() => {
    initializeSVG(componentId, cx);
  }, []);

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
            <ADCBlockDiagram id="adc_03260-main-image"></ADCBlockDiagram>
            <ADCComponentLIst/>  
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
