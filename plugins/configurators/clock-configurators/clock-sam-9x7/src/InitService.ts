import { info } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import { useEffect } from 'react';
import useForceUpdate from 'use-force-update';

export let refreshFullScreen: () => void;

export default function InitService() {
  const update = useForceUpdate();

  const refreshScreen = () => {
    info('refresh screen is called');
    update();
  };

  useEffect(() => {
    info('assigning refreshScreen to refreshFullScreen');
    refreshFullScreen = refreshScreen;
  }, []);

  return {
    refreshScreen
  };
}
