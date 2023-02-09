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
import { Button } from 'primereact/button';
import { Column } from 'primereact/column';
import { DataTable, DataTableRowClassNameOptions } from 'primereact/datatable';

import './channel-table.css';
import { DMAChannel } from '../service/DMAChannel';
import useViewModel from './ChannelsViewModel';

import { COMPONENT_ID } from '../service/DMAService';
import { useBetween } from 'use-between';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import {
  GetSymbolArray,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

export default function ChannelTableView() {
  const {
    activeChannels,
    inactiveChannels,
    addChannel,
    removeSelectedChannel,
    currentChannelNumber,
    setCurrentChannelNumber,
    getCurrentChannel,
  } = useBetween(useViewModel);

  const getChannelNumberCell = (dmaChannel: DMAChannel) => {
    return <span>DMAC Channel {dmaChannel.channelNumber}</span>;
  };

  const isFull = (): boolean => {
    return inactiveChannels().length == 0;
  };
  const isEmpty = (): boolean => {
    return activeChannels().length == 0;
  };

  const isCurrentChannelLocked = (): boolean => {
    return getCurrentChannel()?.locked ?? false;
  };

  const getTriggerCell = (dmaChannel: DMAChannel) => {
    function PriorityBoxChanged(event: { value: any }) {}

    return (
      <DropDown
        key={`${dmaChannel.channelNumber}-${dmaChannel.enabled}-${dmaChannel.locked}`}
        componentId={COMPONENT_ID}
        symbolId={dmaChannel.triggerSourceSymbolID}
        symbolListeners={[dmaChannel.triggerSourceSymbolID]}
        onChange={PriorityBoxChanged}
        symbolValue={GetSymbolValue(
          COMPONENT_ID,
          dmaChannel.triggerSourceSymbolID
        )}
        symbolArray={GetSymbolArray(
          COMPONENT_ID,
          dmaChannel.triggerSourceSymbolID
        )}
        readOnly={dmaChannel.locked}
        styleObject={{ width: '200px', height: '35px' }}
        visible={true}
        className=""
      />
    );
  };

  const getRowClass = (
    dmaChannel: DMAChannel,
    options: DataTableRowClassNameOptions
  ) => {
    return dmaChannel.channelNumber == currentChannelNumber ? 'row-color' : '';
  };

  return (
    <div className="channel-table">
      <h2 className="channel-table-title">Active Channels List</h2>
      <div className="channel-table-content card">
        <DataTable
          value={activeChannels()}
          scrollable
          rowClassName={getRowClass}
          scrollHeight="400px"
          selectionMode="single"
          onSelectionChange={(e) =>
            setCurrentChannelNumber((e.value as DMAChannel).channelNumber)
          }
          emptyMessage={'No Channels are enabled'}
        >
          <Column
            field="channelNumber"
            header="Channel Number"
            headerStyle={{ width: 380 }}
            body={getChannelNumberCell}
          ></Column>
          <Column
            field="trigger"
            header="Trigger"
            body={getTriggerCell}
          ></Column>
        </DataTable>
      </div>
      <div className="button-bar">
        <Button
          type="button"
          className="p-button-raised p-button-rounded"
          label="Add Channel"
          onClick={(e) => addChannel()}
          disabled={isFull()}
        />
        <Button
          type="button"
          className="p-button-raised p-button-rounded"
          label="Remove Selected Channel"
          onClick={removeSelectedChannel}
          disabled={isEmpty() || isCurrentChannelLocked()}
        />
      </div>
    </div>
  );
}
