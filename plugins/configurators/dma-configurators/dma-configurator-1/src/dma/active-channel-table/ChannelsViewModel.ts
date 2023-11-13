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
import {
  AddSymbolListener,
  SetComponentId,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { useEffect, useState } from 'react';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { DMAChannel } from '../service/DMAChannel';
import { dmaService } from '../service/DMAService';
import { ConfigSymbolEvent } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import { log } from '@mplab_harmony/harmony-plugin-core-service';

export default function ChannelsViewModel() {
  const [channels, setChannels] = useState<DMAChannel[]>([]);
  const [currentChannelNumber, setCurrentChannelNumber] = useState(0);

  useEffect(() => {
    SetComponentId('core');

    const dmaChannels = dmaService.allChannels();
    setChannels(dmaChannels);

    setCurrentChannelNumber(
      dmaChannels.find((channel) => channel.enabled)?.channelNumber ?? 0
    );
    registerAllChannelEnableSymbols();
  }, []);

  const registerAllChannelEnableSymbols = () => {
    dmaService.allChannels().forEach((channel) => {
      globalSymbolSStateData.set(channel.enableSymbolID, {
        symbolChanged: symbolChanged,
      });
      globalSymbolSStateData.set(channel.triggerSourceLockSymbolID, {
        symbolChanged: symbolChanged,
      });
      AddSymbolListener(channel.enableSymbolID);
      AddSymbolListener(channel.triggerSourceLockSymbolID);
    });
  };

  const symbolChanged = (symbol: ConfigSymbolEvent) => {
    const channels = dmaService.allChannels();

    const channel = channels.filter(
      (channel) => channel.enableSymbolID === symbol.symbolID
    )[0];

    if (channel) {
      const value = convertToBoolean(symbol.value);
      if (getCurrentChannel()?.enabled == value) return;
      if (convertToBoolean(symbol.value)) {
        setCurrentChannelNumber(channel.channelNumber);
      } else {
        const channelNumberToBeSelected =
          channels.find((channel) => channel.enabled == true)?.channelNumber ??
          0;
        setCurrentChannelNumber(channelNumberToBeSelected);
      }
    }

    setChannels(channels);
  };

  const activeChannels = (): DMAChannel[] => {
    return channels.filter((channel) => channel.enabled);
  };

  const inactiveChannels = (): DMAChannel[] => {
    return channels.filter((channel) => !channel.enabled);
  };

  const nextAvailableChannel = (): DMAChannel | undefined => {
    return channels.find((channel) => !channel.enabled);
  };

  const getCurrentChannel = (): DMAChannel | undefined => {
    return activeChannels().find(
      (channel) => channel.channelNumber === currentChannelNumber
    );
  };

  const addChannel = () => {
    const channelToBeActivated = nextAvailableChannel();

    if (channelToBeActivated == undefined) return;

    dmaService.activateChannel(channelToBeActivated.channelNumber);

    setCurrentChannelNumber(channelToBeActivated.channelNumber);

    const newChannels = channels.map((channel) => {
      if (channel.channelNumber === channelToBeActivated.channelNumber) {
        channel.enabled = true;
      }
      return channel;
    });

    setChannels(newChannels);
  };

  const removeSelectedChannel = () => {
    const currentChannel = getCurrentChannel();
    if (currentChannel == null) return;

    dmaService.deactivateChannel(currentChannel);

    const newChannels = channels.map((channel) => {
      if (channel.channelNumber === currentChannelNumber) {
        channel.enabled = false;
      }
      return channel;
    });
    setChannels(newChannels);

    const channelNumberToBeSelected =
      newChannels.find((channel) => channel.enabled == true)?.channelNumber ??
      0;
    setCurrentChannelNumber(channelNumberToBeSelected);
  };

  return {
    channels,
    activeChannels,
    inactiveChannels,
    addChannel,
    removeSelectedChannel,
    currentChannelNumber,
    setCurrentChannelNumber,
    getCurrentChannel,
  };
}
