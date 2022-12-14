import { Fieldset } from 'primereact/fieldset';
import {
  GetSymbolArray,
  GetSymbolReadOnlyStatus,
  GetSymbolValue,
  UpdateSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  component_id,
  nonSecureColor,
  secureColor,
} from '../MainView/TrustZoneMainView';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';
import { useRef, useState } from 'react';
import { Toast } from 'primereact/toast';
import { Button } from 'primereact/button';
import { GetColorNote } from '../Memory/Memory';

let nonSecureAppendText = '_IS_NON_SECURE';
let secureText = 'Secure';
let nonSecureText = 'Non-Secure';
let warnType = 'warn';
let warningHeading = 'Warning';

const TrustZone = () => {
  const [state, setState] = useState(false);

  let peripehralSymbolArray = GetSymbolArray(
    component_id,
    'TZ_PERIPHERAL_MENU_GUI'
  );
  let mixSecurePeripehralSymbolArray = GetSymbolArray(
    component_id,
    'TZ_MIX_SECURE_PERIPHERAL_MENU_GUI'
  );
  let systemPeripehralSymbolArray = GetSymbolArray(
    component_id,
    'TZ_SYSTEM_RESOURCES_MENU_GUI'
  );

  const toastRef = useRef<any>();

  const showToast = (type: string, header: string, message: any) => {
    toastRef.current.show({
      severity: type,
      summary: header,
      detail: message,
      life: 3000,
    });
  };

  function GetCommonErrorMessage(id: string) {
    let bNonSecure = convertToBoolean(
      GetSymbolValue(component_id, id + nonSecureAppendText)
    );
    let toolTip = secureText;
    if (bNonSecure) {
      toolTip = nonSecureText;
    }
    return id + ' is configured as ' + toolTip + ' .';
  }

  function ShowMixSecureErrorMesssage(id: string) {
    let errorMessage;
    switch (id) {
      case 'PORT':
        errorMessage =
          'Use PIN configurations (UI configurator) to configure PORT Pins.';
        break;
      case 'EVSYS':
        errorMessage =
          'Use EVSYS configurations (UI configurator) to configure Event System.';
        break;
      case 'EIC':
        errorMessage =
          'Use EIC configuration options (tree view) to configure external interrupt controller.';
        break;
      case 'NVMCTRL':
      case 'PAC':
        errorMessage = GetCommonErrorMessage(id);
        break;
      default:
        errorMessage =
          'Configure the require PIN, EIC and EVSYS channel ' +
          'using the respective component (UI configurators).';
        break;
    }
    showToast(warnType, warningHeading, errorMessage);
  }

  function ButtonClicked(butttonText: any) {
    if (mixSecurePeripehralSymbolArray.includes(butttonText)) {
      ShowMixSecureErrorMesssage(butttonText);
      return;
    }
    if (systemPeripehralSymbolArray.includes(butttonText)) {
      showToast(warnType, warningHeading, GetCommonErrorMessage(butttonText));
      return;
    }
    let readOnlyState = GetSymbolReadOnlyStatus(
      component_id,
      butttonText + nonSecureAppendText
    );
    if (readOnlyState) {
      showToast(warnType, warningHeading, GetCommonErrorMessage(butttonText));
      return;
    }
    let symbolId = butttonText + nonSecureAppendText;
    let bNonSecureStatus = convertToBoolean(
      GetSymbolValue(component_id, symbolId)
    );
    UpdateSymbolValue(component_id, symbolId, !bNonSecureStatus);
    setState(!state);
  }

  function GetButtonObject(symbolId: string) {
    let symbolIdStatus = symbolId + nonSecureAppendText;
    let bNonSecure = convertToBoolean(
      GetSymbolValue(component_id, symbolIdStatus)
    );
    let bColor = secureColor;
    let ttip = secureText;
    if (bNonSecure) {
      bColor = nonSecureColor;
      ttip = nonSecureText;
    }
    return (
      <div className="row p-3">
        <Button
          label={symbolId}
          tooltip={ttip}
          tooltipOptions={{ position: 'bottom' }}
          style={{
            width: '120px',
            height: '40px',
            fontSize: '14px',
            fontWeight: 'bold',
            borderWidth: '0px',
            backgroundColor: bColor,
            color: 'white',
          }}
          onClick={() => ButtonClicked(symbolId)}
        />
      </div>
    );
  }

  function AddButton(symbolArray: any) {
    try {
      return (
        <div className="grid">
          {symbolArray.map((id: string) => (
            <div>{GetButtonObject(id)}</div>
          ))}
        </div>
      );
    } catch (err) {}
  }

  return (
    <div>
      <Toast ref={toastRef} position="top-right"></Toast>
      <div className="flex flex-column">
        <div className="p-3">{GetColorNote(20, 'flex flex-row gap-3')}</div>
        <div className="p-3">
          <div className="p-2">
            <Fieldset className="p-3" legend="Peripherals">
              <div>{AddButton(peripehralSymbolArray)}</div>
            </Fieldset>
          </div>

          <div className="p-3">
            <Fieldset className="p-5" legend="Mix-Secure Peripherals">
              <div>{AddButton(mixSecurePeripehralSymbolArray)}</div>
            </Fieldset>
          </div>

          <div className="p-3">
            <Fieldset className="p-5" legend="System Resources">
              <div>{AddButton(systemPeripehralSymbolArray)}</div>
            </Fieldset>
          </div>
        </div>
      </div>
    </div>
  );
};
export default TrustZone;
