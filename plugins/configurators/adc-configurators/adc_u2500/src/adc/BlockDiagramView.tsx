import { ReactComponent as ADCBlockDiagram } from "../images/react_adc_u2500.svg";
import { Dialog } from "primereact/dialog";
import { OverlayPanel } from "primereact/overlaypanel";
import { useContext, useEffect, useRef, useState } from "react";
import { Summary } from "./summary/Summary";
import styles from "./BlockDiagramView.module.css";
import positions from "../styles/positions.module.css";
import {
  usePannableContainer,
  useZoomableContainer,
  useScreehshot,
  PluginToolbar,
  CheckBox,
  PluginConfigContext,
  createClassResolver,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { initializeSVG } from "./SVGhandler";
import GeneralConfiguration from "./generalConfiguration/GeneralConfiguration";
import WindowComparison from "./windowComparison/WindowComparison";
import ChannelSequencer from "./channelSequencer/ChannelSequencer";
import AnalogConfiguration from "./analogConfiguration/AnalogConfiguration";
const cx = createClassResolver(positions, styles);

function BlockDiagramView() {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [summaryPopup, setSummaryPopup] = useState(false);
  const pannableContainer = usePannableContainer();
  const zoomableContainer = useZoomableContainer();
  const enableSlaveCheckBox = useBooleanSymbol({
    componentId,
    symbolId: "ADC_CTRLA_SLAVEEN",
  });

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
            <ADCBlockDiagram id="adc_u2500-main-image"></ADCBlockDiagram>
            {enableSlaveCheckBox.visible && (
              <>
                <CheckBox
                  className={cx("enableSlaveCheckBox")}
                  booleanSymbolHook={enableSlaveCheckBox}
                ></CheckBox>

                <span className={cx("enableSlaveLabel")}>
                  {enableSlaveCheckBox.label}
                </span>
              </>
            )}

            <GeneralConfiguration
              enableSlaveCheckBox={enableSlaveCheckBox.value}
            />
            <WindowComparison />
            <ChannelSequencer />
            <AnalogConfiguration />
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
      </div>
    </div>
  );
}

export default BlockDiagramView;
