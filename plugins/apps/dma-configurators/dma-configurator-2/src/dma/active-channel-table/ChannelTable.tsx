/*******************************************************************************
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
 *******************************************************************************/
import './channel-table.css';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { COMPONENT_ID } from '../service/DMAService';
import { DMAChannel } from '../service/DMAChannel';
import DropDown from 'dma-common/lib/components/DropDown';
import {
  GetSymbolArray,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

import CheckBox from 'dma-common/lib/components/CheckBox';
import { useBetween } from 'use-between';
import ChannelsViewModel from './ChannelsViewModel';

const ChannelTable = () => {
  const { channels, setChannelEnable } = useBetween(ChannelsViewModel);

  const getChannelNumber = (dmaChannel: DMAChannel) => {
    return <span>DMAC Channel {dmaChannel.channelNumber}</span>;
  };

  const ChannelEnableCell = (dmaChannel: DMAChannel) => {
    return (
      <CheckBox
        componentId={COMPONENT_ID}
        symbolId={dmaChannel.enableChannelSymbolID}
        symbolValue={GetSymbolValue(
          COMPONENT_ID,
          dmaChannel.enableChannelSymbolID
        )}
        readOnly={false}
        symbolListeners={[dmaChannel.enableChannelSymbolID]}
        visible={true}
        styleObject={{}}
        className={undefined}
        onChange={(isChecked) => {
          setChannelEnable(dmaChannel, isChecked);
        }}
      />
    );
  };

  const getSimpleDropDown = (symbolID: string, readOnly?: boolean) => {
    function PriorityBoxChanged(event: { value: any }) {}

    if (readOnly == undefined) {
      readOnly = false;
    } else {
      readOnly = !readOnly;
    }

    return (
      <DropDown
        componentId={COMPONENT_ID}
        symbolId={symbolID}
        symbolListeners={[symbolID]}
        onChange={PriorityBoxChanged}
        symbolValue={GetSymbolValue(COMPONENT_ID, symbolID)}
        symbolArray={GetSymbolArray(COMPONENT_ID, symbolID)}
        readOnly={readOnly}
        styleObject={{ width: '100%' }}
        visible={true}
        className=""
      />
    );
  };

  const getSimpleCheckBox = (symbolID: string, readOnly?: boolean) => {
    if (readOnly == undefined) {
      readOnly = false;
    } else {
      readOnly = !readOnly;
    }

    return (
      <CheckBox
        componentId={COMPONENT_ID}
        symbolId={symbolID}
        symbolValue={GetSymbolValue(COMPONENT_ID, symbolID)}
        readOnly={readOnly}
        symbolListeners={[symbolID]}
        visible={true}
        styleObject={{}}
        className={undefined}
        onChange={function (arg0: any): void {}}
      />
    );
  };

  return (
    <div className="channel-table">
      <h2 className="channel-table-title">DMA Channels List</h2>
      <div className="channel-table-content card">
        <DataTable value={channels} responsiveLayout="scroll">
          <Column
            field="channelNumber"
            header="Channel Number"
            body={getChannelNumber}
          ></Column>
          <Column
            field="enableChannelll"
            header="Enable"
            align="center"
            body={ChannelEnableCell}
          ></Column>
          <Column
            field="trigger"
            header="Trigger"
            style={{ width: '255px' }}
            body={(dmaChannel: DMAChannel) =>
              getSimpleDropDown(
                dmaChannel.triggerSourceSymbolID,
                dmaChannel.enabled && !dmaChannel.locked
              )
            }
          ></Column>
          <Column
            field="priority"
            header="Priority"
            body={(dmaChannel: DMAChannel) =>
              getSimpleDropDown(dmaChannel.prioritySymbolID, dmaChannel.enabled)
            }
          ></Column>
          <Column
            field="interruptEnable"
            header="Interrupt Enable"
            align="center"
            body={(dmaChannel: DMAChannel) =>
              getSimpleCheckBox(
                dmaChannel.enableInterruptSymbolID,
                dmaChannel.enabled
              )
            }
          ></Column>
        </DataTable>
      </div>
    </div>
  );
};

export default ChannelTable;
