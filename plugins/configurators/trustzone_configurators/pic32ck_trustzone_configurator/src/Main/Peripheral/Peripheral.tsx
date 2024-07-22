import { Fieldset } from 'primereact/fieldset';
import { useContext, useRef } from 'react';
import { Toast } from 'primereact/toast';
import { GetColorNote } from '../Memory/Memory';
import PeripheralButton from './PeripheralButton';
import { PluginConfigContext, useComboSymbol } from '@mplab_harmony/harmony-plugin-client-lib';

let nonSecureAppendText = '_IS_NON_SECURE';
let secureText = 'Secure';
let nonSecureText = 'Non-Secure';
let warnType = 'warn';
let warningHeading = 'Warning';

const TrustZone = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const peripehralSymbol = useComboSymbol({
    componentId: componentId,
    symbolId: 'TZ_PERIPHERAL_MENU_GUI'
  });
  const mixSecurePeripehralSymbol = useComboSymbol({
    componentId: componentId,
    symbolId: 'TZ_MIX_SECURE_PERIPHERAL_MENU_GUI'
  });
  const systemPeripehralSymbol = useComboSymbol({
    componentId: componentId,
    symbolId: 'TZ_SYSTEM_RESOURCES_MENU_GUI'
  });

  const toastRef = useRef<any>();

  const showToast = (type: string, header: string, message: any) => {
    toastRef.current.show({
      severity: type,
      summary: header,
      detail: message,
      life: 5000
    });
  };

  function ButtonClicked(butttonText: string, symbolValue: boolean, readOnlyState: boolean) {
    if (mixSecurePeripehralSymbol.options.includes(butttonText)) {
      showToast(warnType, warningHeading, GetMixSecureErrorMesssage(butttonText, symbolValue));
      return false;
    }
    if (systemPeripehralSymbol.options.includes(butttonText)) {
      showToast(warnType, warningHeading, GetCommonErrorMessage(butttonText, symbolValue));
      return false;
    }
    if (readOnlyState) {
      showToast(warnType, warningHeading, GetCommonErrorMessage(butttonText, symbolValue));
      return false;
    }
    return true;
  }

  function GetCommonErrorMessage(id: string, symbolValue: boolean) {
    let toolTip = secureText;
    if (symbolValue) {
      toolTip = nonSecureText;
    }
    return id + ' is configured as ' + toolTip + ' .';
  }

  function GetMixSecureErrorMesssage(id: string, symbolValue: boolean) {
    let errorMessage;
    switch (id) {
      case 'PORT':
        errorMessage = 'Use PIN configurations (UI configurator) to configure PORT Pins.';
        break;
      case 'EVSYS':
        errorMessage = 'Use EVSYS configurations (UI configurator) to configure Event System.';
        break;
      case 'EIC':
        errorMessage =
          'Use EIC configuration options (tree view) to configure external interrupt controller.';
        break;
      case 'NVMCTRL':
      case 'PAC':
        errorMessage = GetCommonErrorMessage(id, symbolValue);
        break;
      default:
        errorMessage =
          'Configure the require PIN, EIC and EVSYS channel ' +
          'using the respective component (UI configurators).';
        break;
    }
    return errorMessage;
  }

  return (
    <div>
      <Toast
        ref={toastRef}
        position='top-right'></Toast>
      <div className='flex flex-column'>
        <div className='p-3'>{GetColorNote(20, 'flex flex-row gap-3')}</div>
        <div className='p-3'>
          <div className='p-2'>
            <Fieldset
              className='p-3'
              legend='Peripherals'>
              <div className='grid'>
                {peripehralSymbol.options.map((id: string) => (
                  <div>
                    <PeripheralButton
                      key={id}
                      componentId={componentId}
                      symbolId={id}
                      nonSecureAppendText={nonSecureAppendText}
                      secureText={secureText}
                      nonSecureText={nonSecureText}
                      ButtonClicked={ButtonClicked}
                    />
                  </div>
                ))}
              </div>
            </Fieldset>
          </div>

          <div className='p-3'>
            <Fieldset
              className='p-5'
              legend='Mix-Secure Peripherals'>
              <div className='grid'>
                {mixSecurePeripehralSymbol.options.map((id: string) => (
                  <div>
                    <PeripheralButton
                      key={id}
                      componentId={componentId}
                      symbolId={id}
                      nonSecureAppendText={nonSecureAppendText}
                      secureText={secureText}
                      nonSecureText={nonSecureText}
                      ButtonClicked={ButtonClicked}
                    />
                  </div>
                ))}
              </div>
            </Fieldset>
          </div>

          <div className='p-3'>
            <Fieldset
              className='p-5'
              legend='System Resources'>
              <div className='grid'>
                {systemPeripehralSymbol.options.map((id: string) => (
                  <div>
                    <PeripheralButton
                      key={id}
                      componentId={componentId}
                      symbolId={id}
                      nonSecureAppendText={nonSecureAppendText}
                      secureText={secureText}
                      nonSecureText={nonSecureText}
                      ButtonClicked={ButtonClicked}
                    />
                  </div>
                ))}
              </div>
            </Fieldset>
          </div>
        </div>
      </div>
    </div>
  );
};
export default TrustZone;
