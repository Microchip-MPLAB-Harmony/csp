/*
 * Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software
 * and any derivatives exclusively with Microchip products. It is your
 * responsibility to comply with third party license terms applicable to your
 * use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
 * PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
 * ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 */

import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { useContext, useEffect, useState } from "react";
import {
  CheckBoxDefault,
  DropDownDefault,
  InputNumberDefault,
  PluginConfigContext,
  symbolApi,
  symbolUtilApi,
  useBooleanSymbol,
  useComboSymbol,
  useStringSymbol,
  useSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const GenericClockConfiguration = () => {
  const { componentId = "core" } = useContext(PluginConfigContext);

  const gclk_ids = useComboSymbol({
    componentId,
    symbolId: "GCLK_IO_CLOCK_CONFIG_UI",
  });
  let channelPeripipheralMap = gclk_ids.options;
  let customLabelsArray = createCustomLengthArray();

  function createCustomLengthArray() {
    let dataArr = [];
    for (let i = 0; i < channelPeripipheralMap.length; i++) {
      dataArr.push({ id: i });
    }
    return dataArr;
  }

  const PeripheralBodyTemplate = (rowData: any) => {
    // const stringSymbol = useStringSymbol({
    //   componentId: componentId,
    //   symbolId: channelPeripipheralMap[rowData.id]
    // });
    return <div>{channelPeripipheralMap[rowData.id]}</div>;
  };

  const PeripheralEnableBodyTemplate = (rowData: any) => {
    return (
      <div>
        <CheckBoxDefault
          componentId={componentId}
          symbolId={channelPeripipheralMap[rowData.id] + "_CLOCK_ENABLE"}
        />
      </div>
    );
  };
  const GenericEnableBodyTemplate = (rowData: any) => {
    const [fallback, setFallback] = useState(false);
    symbolApi
      .getSymbol(
        componentId,
        channelPeripipheralMap[rowData.id] + "_GCLK_ENABLE"
      )
      .then(() => setFallback(true))
      .catch((e) => {
        setFallback(false);
      });
    if (fallback) {
      return (
        <div>
          <CheckBoxDefault
            componentId={componentId}
            symbolId={channelPeripipheralMap[rowData.id] + "_GCLK_ENABLE"}
          />
        </div>
      );
    } else {
      return <div><i className="pi pi-times" style={{ fontSize: '1.5rem' }}></i></div>;
    }
  };

  const GCLKSourceBodyTemplate = (rowData: any) => {
    const [fallback, setFallback] = useState(false);
    symbolApi
      .getSymbol(componentId, channelPeripipheralMap[rowData.id] + "_GCLK_CSS")
      .then(() => setFallback(true))
      .catch((e) => {
        setFallback(false);
      });
    if (fallback) {
      return (
        <div>
          <DropDownDefault
            componentId={componentId}
            symbolId={channelPeripipheralMap[rowData.id] + "_GCLK_CSS"}
          />
        </div>
      );
    } else {
      return <div><i className="pi pi-times" style={{ fontSize: '1.5rem' }}></i></div>;
    }
  };
  const GCLKDIVBodyTemplate = (rowData: any) => {
    const [fallback, setFallback] = useState(false);
    symbolApi
      .getSymbol(componentId, channelPeripipheralMap[rowData.id] + "_GCLK_DIV")
      .then(() => setFallback(true))
      .catch((e) => {
        setFallback(false);
      });
    if (fallback) {
      return (
        <div>
          <InputNumberDefault
            componentId={componentId}
            symbolId={channelPeripipheralMap[rowData.id] + "_GCLK_DIV"}
          />
        </div>
      );
    } else {
      return <div><i className="pi pi-times" style={{ fontSize: '1.5rem' }}></i></div>;
    }
  };

  const GCLKFrequencyBodyTemplate = (rowData: any) => {
    const [fallback, setFallback] = useState(false);
    symbolApi
      .getSymbol(
        componentId,
        channelPeripipheralMap[rowData.id] + "_GCLK_FREQUENCY"
      )
      .then(() => setFallback(true))
      .catch((e) => {
        setFallback(false);
      });
    if (fallback) {
      return (
        <div>
          <FrequencyLabelComponent
            componentId={componentId}
            symbolId={channelPeripipheralMap[rowData.id] + "_GCLK_FREQUENCY"}
            className={""}
          />
        </div>
      );
    } else {
      return <div><i className="pi pi-times" style={{ fontSize: '1.5rem' }}></i></div>;
    }
  };
  const PeripheralFrequencyBodyTemplate = (rowData: any) => {
    const [fallback, setFallback] = useState(false);
    symbolApi
      .getSymbol(
        componentId,
        channelPeripipheralMap[rowData.id] + "_CLOCK_FREQUENCY"
      )
      .then(() => setFallback(true))
      .catch((e) => {
        setFallback(false);
      });
    if (fallback) {
      return (
         <div>
        <FrequencyLabelComponent
          componentId={componentId}
          symbolId={channelPeripipheralMap[rowData.id] + "_CLOCK_FREQUENCY"}
          className={""}
        />
      </div>
      );
    } else {
      return <div>0 Hz</div>;
    }
    
  };

  return (
    <div>
      <DataTable value={customLabelsArray} style={{ minWidth: "650px" }}>
        <Column
          field="Peripheral"
          header="Peripheral"
          body={PeripheralBodyTemplate}
        ></Column>
        <Column
          field="peripheralClockEnable"
          header="Peripheral Clock Enable"
          body={PeripheralEnableBodyTemplate}
          style={{textAlign:'center'}}
        ></Column>
        <Column
          field="genericClockEnable"
          header="Generic Clock Enable"
          body={GenericEnableBodyTemplate}
          style={{textAlign:'center'}}
        ></Column>
        <Column
          field="gclkSource"
          header="GCLK Source"
          body={GCLKSourceBodyTemplate}
          style={{textAlign:'center'}}
        ></Column>
        <Column
          field="gclkDiv"
          header="GCLK DIV"
          body={GCLKDIVBodyTemplate}
          style={{textAlign:'center'}}
        ></Column>

        <Column
          field="gclkFrequency"
          header="GCLK Frequency"
          body={GCLKFrequencyBodyTemplate}
          style={{textAlign:'center'}}
        ></Column>
        <Column
          field="peripheralFrequency"
          header="Peripheral Frequency"
          body={PeripheralFrequencyBodyTemplate}
          style={{textAlign:'center'}}
        ></Column>
      </DataTable>
    </div>
  );
};
export default GenericClockConfiguration;
