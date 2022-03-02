import { Accordion, AccordionTab } from "primereact/accordion";
import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
import {
  GetSymbolArray,
  GetSymbolLabelName,
  GetSymbolValue,
} from "../../Common/SymbolAccess";
import { component_id } from "./MainBlock";

const SummaryPage = () => {
  function GetLabelAndValue(
    labelName: string,
    symbolId: string,
    appendString: string = ""
  ) {
    return (
      <div className="p-field p-grid">
        <div>
          <label style={{ fontSize: "14px" }} className="p-col">
            {" "}
            {"\u2022 " + labelName + " : "}
          </label>
        </div>
        <div className="p-col">
          <label style={{ fontSize: "14px" }} className="p-col">
            {GetSymbolValue(component_id, symbolId) + appendString}{" "}
          </label>
        </div>
      </div>
    );
  }

  function SlowClockSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("External Clock Enable", "CLK_OSC32EN")}
        {GetLabelAndValue("External Clock Frequency", "CLK_OSC32BYP_FREQ")}
        {GetLabelAndValue("CLK_OSC32BYP", "CLK_OSC32BYP")}
        {GetLabelAndValue("Oscillator Select", "CLK_TD_OSCSEL")}
        {GetLabelAndValue(
          "MD Slow clock Frequency",
          "MD_SLOW_CLK_FREQUENCY",
          " Hz"
        )}

        {GetLabelAndValue(
          "TD Slow clock Frequency",
          "TD_SLOW_CLOCK_FREQUENCY",
          " Hz"
        )}
      </div>
    );
  }

  function MainClockSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("Embedded 12MHz Osc Enable", "CLK_MOSCXTEN")}
        {GetLabelAndValue("External Osc Enable", "CLK_MOSCXTEN")}
        {GetLabelAndValue("External clock Freqency", "CLK_MOSCXT_FREQ", " Hz")}
        {GetLabelAndValue("Startup time", "CLK_MOSCXTST")}
        {GetLabelAndValue("Main Osc Select", "CLK_MOSCSEL")}
        {GetLabelAndValue("Main Clock Frequency", "MAINCK_FREQUENCY", " Hz")}
      </div>
    );
  }

  function PLLAControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("Multiplier", "CLK_PLLA_MUL")}
        {GetLabelAndValue("FRACR", "CLK_PLLA_FRACR")}
        {GetLabelAndValue("DIVPMC", "CLK_PLLA_DIVPMC")}
        {GetLabelAndValue("PLLA Enable", "CLK_PLLA_EN")}
        {GetLabelAndValue("PLLADIV2 Enable", "CLK_PLLADIV2_EN")}
        {GetLabelAndValue("PLLA clock Freqency", "PLLA_FREQUENCY", " Hz")}
        {GetLabelAndValue(
          "PLLADIV2 Clock Frequency",
          "PLLADIV2CLK_FREQUENCY",
          " Hz"
        )}
      </div>
    );
  }

  function UPLLControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("UPLL Enable", "CLK_UPLL_EN")}
        {GetLabelAndValue("Multiplier", "CLK_UPLL_MUL")}
        {GetLabelAndValue("FRACR", "CLK_UPLL_FRACR")}
      </div>
    );
  }

  function AUDIOPLLControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("AUDIOPLL Enable", "CLK_AUDIOPLL_EN")}
        {GetLabelAndValue("Multiplier", "CLK_AUDIOPLL_MUL")}
        {GetLabelAndValue("FRACR", "CLK_AUDIOPLL_FRACR")}
        {GetLabelAndValue("DIVPMC", "CLK_AUDIOPLL_DIVPMC")}
        {GetLabelAndValue("DIVIO", "CLK_AUDIO_IOPLLCK_DIVIO")}
        {GetLabelAndValue("IOPLLCK Enable", "CLK_AUDIO_IOPLLCK_EN")}
        {GetLabelAndValue("AUDIOPLL Frquency", "AUDIOPLL_FREQUENCY", " Hz")}
        {GetLabelAndValue(
          "AUDIO IOPLLCK Frquency",
          "AUDIO_IOPLLCK_FREQUENCY",
          " Hz"
        )}
      </div>
    );
  }

  function LVDSPLLControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("Multiplier", "CLK_LVDSPLL_MUL")}
        {GetLabelAndValue("FRACR", "CLK_LVDSPLL_FRACR")}
        {GetLabelAndValue("DIVPMC", "CLK_LVDSPLL_DIVPMC")}
        {GetLabelAndValue("LVDSPLL Enable", "CLK_LVDSPLL_EN")}
        {GetLabelAndValue("LVDSPLL Frequency", "LVDSPLL_FREQUENCY", " Hz")}
      </div>
    );
  }

  function processorClockControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("CSS", "CLK_CPU_CKR_CSS")}
        {GetLabelAndValue("PRES", "CLK_CPU_CKR_PRES")}
        {GetLabelAndValue("MDIV", "CLK_CPU_CKR_MDIV")}
        {GetLabelAndValue("DDR Enable", "CLK_DDR_ENABLE")}
        {GetLabelAndValue("QSPICLK Enable", "CLK_QSPICLK_ENABLE")}
        {GetLabelAndValue("CPU clock Frequency", "CPU_CLOCK_FREQUENCY", " Hz")}
        {GetLabelAndValue("DDR clock Frequency", "DDRCLK_FREQUENCY", " Hz")}
        {GetLabelAndValue(
          "QSPI clock Frequency",
          "QSPI_CLOCK_FREQUENCY",
          " Hz"
        )}
        {GetLabelAndValue("MCK clock Frequency", "MCK_FREQUENCY", " Hz")}
      </div>
    );
  }

  function programmableClkControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("PCLK0 CSS", "CLK_PCK0_CSS")}
        {GetLabelAndValue("PCLK0 PRES", "CLK_PCK0_PRES")}
        {GetLabelAndValue("PCLK0 Enable", "CLK_PCK0_EN")}
        {GetLabelAndValue("PCLK0 Frequency", "CLK_PCK0_FREQUENCY", " Hz")}
        {GetLabelAndValue("PCLK1 CSS", "CLK_PCK1_CSS")}
        {GetLabelAndValue("PCLK1 PRES", "CLK_PCK1_PRES")}
        {GetLabelAndValue("PCLK1 Enable", "CLK_PCK1_EN")}
        {GetLabelAndValue("PCLK1 Frequency", "CLK_PCK1_FREQUENCY", " Hz")}
      </div>
    );
  }

  function USBClockControllerSettings() {
    return (
      <div className="p-d-flex p-flex-column">
        {GetLabelAndValue("USB Select", "CLK_USB_USBS")}
        {GetLabelAndValue("USB DIV", "CLK_USB_USBDIV")}
        {GetLabelAndValue("USB Enable", "CLK_USB_EN")}
        {GetLabelAndValue("UHP48M", "CLK_UHP48M")}
      </div>
    );
  }

  function GetPeripheralClockConfig() {
    let channelPeripipheralMap = GetSymbolArray(
      component_id,
      "PERIPHERAL_CLOCK_CONFIG"
    );

    function getChannelPeripheralCols() {
      let colsJsx = [];
      let cols = channelPeripipheralMap.length / 10;
      if (channelPeripipheralMap % 10 < 0) {
        cols = cols + 1;
      }

      for (let i: number = 0; i < cols; i++) {
        let start: number = 10 * i;
        let end: number = start + 10;
        if (end >= channelPeripipheralMap.length) {
          end = channelPeripipheralMap.length - 1;
        }
        colsJsx.push(getColumn(start, end));
      }
      return colsJsx;
    }

    function getColumn(startIndex: number, endIndex: number) {
      return (
        <div className="p-field">
          <div className="p-fluid">
            {getSymbolWithLabels(startIndex, endIndex)}
          </div>
        </div>
      );
    }

    function getSymbolWithLabels(startIndex: number, endIndex: number) {
      const arrLabelName = [];
      for (let i: number = startIndex; i < endIndex; i++) {
        arrLabelName.push(
          <div>
            {GetLabelAndValue(
              GetSymbolLabelName(component_id, channelPeripipheralMap[i]) +
                " Enabled: ",
              channelPeripipheralMap[i]
            )}
          </div>
        );
      }
      return arrLabelName;
    }

    return (
      <div className="p-formgroup-inline">{getChannelPeripheralCols()}</div>
    );
  }

  function GetGenericClockConfig() {
    let channelPeripipheralMap = GetSymbolArray(
      component_id,
      "GCLK_INSTANCE_PID"
    );
    let customLabelsArray = createCustomLengthArray();

    function createCustomLengthArray() {
      let dataArr = [];
      for (let i = 0; i < channelPeripipheralMap.length; i++) {
        dataArr.push({ id: i });
      }
      return dataArr;
    }

    const PeripheralBodyTemplate = (rowData: any) => {
      return <div>{channelPeripipheralMap[rowData.id]}</div>;
    };

    const EnableBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            "CLK_" + channelPeripipheralMap[rowData.id] + "_GCLKEN"
          )}
        </div>
      );
    };

    const SourceBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            "CLK_" + channelPeripipheralMap[rowData.id] + "_GCLKCSS"
          )}
        </div>
      );
    };

    const DivisorBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            "CLK_" + channelPeripipheralMap[rowData.id] + "_GCLKDIV"
          )}
        </div>
      );
    };

    const FrequencyBodyTemplate = (rowData: any) => {
      return (
        <div>
          {GetSymbolValue(
            component_id,
            channelPeripipheralMap[rowData.id] + "_GCLK_FREQUENCY"
          ) + " Hz"}
        </div>
      );
    };

    return (
      <div className="p-formgroup-inline">
        <div className="p-d-flex">
          <div className="card">
            <DataTable
              value={customLabelsArray}
              stripedRows
              showGridlines
              responsiveLayout="scroll"
            >
              <Column
                field="Peripheral"
                header="Peripheral"
                body={PeripheralBodyTemplate}
              ></Column>
              <Column
                field="Enable"
                header="Enable"
                body={EnableBodyTemplate}
              ></Column>
              <Column
                field="Source"
                header="Source"
                body={SourceBodyTemplate}
              ></Column>
              <Column
                field="Divisor"
                header="Divisor"
                body={DivisorBodyTemplate}
              ></Column>
              <Column
                field="Frequency"
                header="Frequency"
                body={FrequencyBodyTemplate}
              ></Column>
            </DataTable>
          </div>
        </div>
      </div>
    );
  }

  function GetClockConfig() {
    return (
      <div className="p-formgroup-inline">
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                Slow clock{" "}
              </span>
            </div>
            <div className="p-field">{SlowClockSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                Main clock{" "}
              </span>
            </div>
            <div className="p-field">{MainClockSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                PLLA Controller{" "}
              </span>
            </div>
            <div className="p-field">{PLLAControllerSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                UPLL Controller{" "}
              </span>
            </div>
            <div className="p-field">{UPLLControllerSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                AUDIO PLL Controller{" "}
              </span>
            </div>
            <div className="p-field">{AUDIOPLLControllerSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                LVDSPLL Controller{" "}
              </span>
            </div>
            <div className="p-field">{LVDSPLLControllerSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                Processor Clock Controller{" "}
              </span>
            </div>
            <div className="p-field">{processorClockControllerSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                Programmable clock Controller{" "}
              </span>
            </div>
            <div className="p-field">{programmableClkControllerSettings()}</div>
          </div>
        </div>
        <div className="p-field">
          <div className="p-fluid">
            <div className="p-field">
              <br></br>
              <span style={{ fontWeight: "bold", fontSize: "14px" }}>
                {" "}
                USB clock Controller{" "}
              </span>
            </div>
            <div className="p-field">{USBClockControllerSettings()}</div>
          </div>
        </div>
      </div>
    );
  }

  // function getAcordian() {
  //   return (

  //   );
  // }

  return (
    <div>
      <Accordion activeIndex={0}>
        <AccordionTab header="Clock Configuration">
          <div className="p-d-flex p-flex-column">{GetClockConfig()}</div>
        </AccordionTab>
        <AccordionTab header="Peripheral Clock Configuration">
          <div className="p-d-flex p-flex-column">
            {GetPeripheralClockConfig()}
          </div>
        </AccordionTab>
        <AccordionTab header="Generic Clock Configuration">
          <div className="p-d-flex p-flex-column">
            {GetGenericClockConfig()}
          </div>
        </AccordionTab>
      </Accordion>
    </div>
  );
};

export default SummaryPage;
