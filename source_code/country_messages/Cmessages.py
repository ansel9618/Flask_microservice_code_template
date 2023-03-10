class Messages:
    #AUTH MESSAGES
    EXPIRED_AUTH_HEADER = "Session Timeout"
    INVALID_AUTH_HEADER = "Authorization token is invalid in headers"
    AUTH_MISSING_HEADER = "Auth token missing in the header"
    STAGING_SUCCESS = "Successfully updated staging details"
    application_does_not_exist = "Application does not exist"
    incorrect_date_time_format = "Incorrect data format, should be YYYY-MM-DD"
    FAILED_TO_GET_USER_UUID = "Failed to get user uuid"
    failed_to_get_citizencategory_type = "failed to get citizen_category type"
    failed_to_set_inapp_notification ="failed to set in app notification"
    NOTIFICATION_SETUP_SUCCESS = "Notification setup successfully"
    NOTIFICATION_SETUP_FAIL = "Notification setup failed"

    failed_tofetch_reference_id = "Failed to fetch reference id"
    failed_to_get_account_details = "Failed to get account details"
    failed_to_get_fincity_token = "Failed to get fincity token"
    Phone_no_update_success = "Successfully updated ph_no in I2C & database"
    email_update_success = "Successfully updated email in I2C & database"

    successfully_retrieved_user_profile="successfully retrieved user profile info"
    SUCCESS_UPDATE_REFERENCE_ID="Reference id updated successfully"
    FAILURE_UPDATE_REFERENCE_ID = "Failed to update Reference id"
    failed_to_retrieve_user_profile = "failed retrieved user profile info"
    user_uuid_doesnotexist_inapplication="user_uuid does not exist in application table"
    saved_bank_account_details = "Saved bank account details from i2c"
    failed_tosave_bank_account_details = "Failed to save bank account deatails from i2c"
    customer_id_exist = "customer id exist in fincity customer table"
    customer_id_not_exist = "customer id does not exists"
    user_uuid_doesnotexist = "user_uuid does not exist in fincity customer_account table"
    user_uuid_doesnotexist_get_user_info="failed to get user info"
    account_no_already_exist = "Account no already exist in i2c_bank_account_detail"
    failed_toget_i2c_bank_details = "Failed to get i2c bank details"
    i2c_bank_details_inserted = "Successfully inserted i2c bank details"
    failed_to_get_useruuid="failed to get uer_uuid from get_user_details"
    access_tokem_customerid_nomatch = "access token and customerid does not match"
    customer_account_not_found = " Finicity api to get customer account Failed"
    uuid_application_not_exist = "uuid does not exist in application table"

    update_bank_account_failed = "Bank account update is failed"
    failed_to_update = "failed to update data"
    failed_to_update_i2c_phno = "failed to update ph_no in i2c"
    failed_to_update_db_phno = "failed to update ph_no in database"
    failed_to_update_i2c_email = "failed to update email in i2c"
    failed_to_update_db_email = "failed to update email in database"
    failed_to_save_address = "failed to update address in database table address"
    address_update_success="successfully updated address in I2c and database_onboarding_address_table"
    failed_to_update_i2c_address ="failed to update address in I2c "
    FAILED = "failed"
    FALSE = False
    OTP_VERIFICATION_FAILED = "Failed to verify OTP"
    SUCCESS = "Success"
    TRUE = True
    INTERNAL_ERROR = "Internal server error occurred"
    TIME_LIMIT_EXCEEDED = "Time limit exceeded"
    USER_UUID_NOT_PRESENT = "User needs to start application"
    SAVED_NEW_USER = "Saved new user details"
    STATES_LISTED_SUCCESS = "Successfully got all states"
    NO_DATA_TO_GET = "No data to get"
    COUNTRIES_LISTED_SUCCESS = "Successfully got all countries"
    INTIMATION_TYPE_SUCCESS = "Successfully got intimation_type"
    VERIFICATION_TYPE = "Successfully got verification_type"
    USER_VERIFICATION_DETAILS_SUCCESS = "successfully got all user verification details"
    OCCUPATION_LIST_SUCCESS = "Successfully got all occupation"
    OCCUPATION_LIST_FAILED = "Failed to get all occupation in database"
    CITIES_LISTED_SUCCESS = "Successfully got state and city"
    NO_CITY_FOUND = "No state and city found for the given zip code"
    CITY_LISTED_SUCCESS = "Successfully got all state and city"
    UNEMPLOYMENT_LIST_SUCCESS = "Successfully got unemployed education list"
    UNEMPLOYMENT_LIST_FAILED = "No unemployment list available"
    GET_SCHOOLS_STATE_SUCCESS = "Successfully got major list with schools in state"
    GET_SCHOOLS_STATE_FAILED = "No major list of schools available"
    GET_USER_DETAILS_SUCCESS = "Successfully retrieved user details"
    GET_USER_DETAILS_FAILED = "Failed to retrieve user details"
    GET_AGREEMENT_POLICY_TERMS_SUCCESS = "Successfully retrieved terms condition and privacy policy"
    GET_AGREEMENT_POLICY_TERMS_FAILURE = "Failed retrieved terms condition and privacy policy"
    GET_CITIZENSHIP_INFO_SUCCESS = "Successfully retrieved citizenship info"
    GET_APPLICATION_LIST_SUCCESS = "Successfully retrieved all the standard application list"
    FAILED_TO_GET_APPLICATION_LIST = "Failed to retrieve the standard application list"
    GET_ENROLLMENT_INFO_SUCCESS = "Successfully retrieved enrollment info"
    STUDENT_LIST_SUCCESS = "Successfully retrieved student info"
    EMPLOYED_LIST = "Successfully retrieved employment list"
    CITY_STATE_ZIP_SUCCESS = "Zip code is matching with state and city"
    CITY_STATE_ZIP_FAILED = "Zip code is not matching with state and city"
    COUNTRY_LIST_SUCCESS= "Successfully retrieved country list"
    STAGE_LIST_FAILED = "Failed to retrieved stage list"
    GET_CONNECT_URL_SUCCESS = "Link generated succesfully"
    FAILED_TO_GET_UUID = "Failed to get user uuid from Auth0"
    BANK_ACCOUNT_SET_AS_DEFAULT = "Bank account set as default"
    USER_UUID_NOT_IN_DB = "User uuid not present in the database"
    USER_BANK_UUID_NOT_IN_DB = "User bank account details uuid not present in database"
    BANK_ACCOUNT_INFO_FETCHED_SUCCESSFULLY = "Bank account details fetched successfully"

#update application stage
    APPLICATION_UUID_updated = "Stage id updated"
    APPLICATION_UUID_NOT_EXISTS= "Application uuid does not exist in application table"
    USER_UUID_INSERTED_FOR_REAPPLICATION = "User id inserted for reapplication"
#save user details table
    USER_UUID_INSERTED = "user_uuid successfully saved in application table"
    USER_UUID_EXISTS = "user_uuid exists in application table"
    DOB_SAVED ="date of birth saved"
    DOB_SAVE_FAILED ="date of birth save failed"
    ENTER_FIELDS_PROPERLY ="Enter fields in proper format"

    PRI_ADDRESS_SAVED = "Primary Address saved"
    PRI_ADDRESS_UPDATE_SAVE = "Primary Address update saved"
    PRI_ADDRESS_VALUE_EMPTY = "Primary address values empty"
    ADDRESS_SAVE_FAIL = "Address Save Fail"
    SHIP_ADDRESS_SAVED = "Shipping Address Saved"
    SHIP_ADDRESS_UPDATE_SAVE = "shipping Address update saved"
    SHIP_ADDRESS_VALUE_EMPTY = "shipping  address values empty"
    failed_to_save_address_pri_id = "failed to save address primary id"
    failed_to_save_address_ship_id = "failed to save address shipping id"
    user_address_does_not_exist = "user address does not exist in address table"

    CITIZENSHIP_TYPE_SAVED = "Citizenship type saved"
    CITIZENSHIP_TYPE_UPDATE_SAVED = "Citizenship type update saved"
    CITIZENSHIP_TYPE_VALUE_EMPTY = "Citizen type value empty"
    CITIZENSHIP_TYPE_SAVE_FAIL = "Citizenship type save failed"

    CITIZENSHIP_IDENTIFICATION = "Saved citizenship identification"
    CITIZENSHIP_IDENTIFICATION_FAIL = "Citizenship identification fail"
    CITIZENSHIP_TYPE_FAIL = "Citizenship type id does not exist"
    CITIZENSHIP_IDENTIFICATION_VALUE_EMPTY = "Citizen identification values empty"
    NO_ZIP_CODE = "Enter a valid Zip code"

    ENROLLMENT_TYPE_SAVED = "Enrollment type saved"
    ENROLLMENT_TYPE_UPDATE_SAVED = "Enrollment type update saved"
    ENROLLMENT_TYPE_SAVE_FAIL = "Enrollment type save Fail enter proper type id"
    ENROLLMENT_TYPE_VALUE_EMPTY = "Enrollment type value empty"

    MONTHLY_INCOME_SAVED= "Monthly income saved"
    MONTHLY_INCOME_SAVE_FAILED = "Monthly income save failed"
    MONTHLY_INCOME_VALUE_EMPTY= "Monthly income value empty"

    MONTHLY_EXPENSE_SAVED = "Monthly expense and iovation_blackbox saved successfully"
    MONTHLY_EXPENSE_SAVE_FAILED = "Monthly expense save failed"
    EXPENSE_GREATER_THAN_INCOME ="Monthly expense greater than income ,monthly expense save failed"
    MONTHLY_EXPENSE_VALUE_EMPTY = "Monthly expense value empty"

    ENTER_KEY_VALUE_PROPERLY = "Enter Keys and values in request in proper specified format"

    EMPLOYMENT_STATUS_SAVED = "Employment_status saved"
    EMPLOYMENT_TYPE_UPDATE_SAVED = "Employment type update saved"
    EMPLOYMENT_STATUS_SAVE_FAIL = "Employment_status save failed"
    EMPLOYMENT_STATUS_VALUE_EMPTY = "Employment_status value empty"

    identification_type_saved = "Identification type data saved"
    identification_data_save_fail = "Identification data save fail"
    identity_data_save_failed_no_user = "Data cannot be saved since user does not exist"
    identification_data_empty = "Identification data values empty"

    UNEMPLOYED_EDUCATION_TYPE_SAVED = "Unemployed education type saved "
    UNEMPLOYED_EDUCATION_TYPE_SAVE_FAIL = "Unemployed education type save fail"
    UNEMPLOYED_EDUCATION_TYPE_VALUE_EMPTY = "Unemployed education type value empty"
    UNEMPLOYED_EDUCATION_TYPE_SAVE_FAILED= "Failed to save data in table since application id does not exist education_details table"
    PRIOR_OCCUPATION_ID_SAVED = "Prior occupation id saved"
    PRIOR_OCCUPATION_ID_SAVE_FAIL = "Failed to save data in table since application id does not exist employement_details table"
    PRIOR_OCCUPATION_ID_VALUE_EMPTY = "Prior occupation id value empty"

    OCCUPATION_ID_SAVED = "Occupation id saved"
    OCCUPATION_ID_SAVE_FAIL ="Failed to save data in table since application id does not exist employement_details table"
    OCCUPATION_ID_VALUE_EMPTY = "Occupation id value empty"

    STUDENT_INFO_SAVED = "Student info id saved"
    STUDENT_INFO_SAVE_FAIL = " Failed to save data in table since application id does not exist education_details table"
    STUDENT_INFO_VALUE_EMPTY = " Student info  value empty"

    SCHOOL_INFO_SAVED = "School id  and grant type saved"
    SCHOOL_INFO_SAVE_FAIL = " Failed to save data in table since application id does not exist education_details table"
    SCHOOL_INFO_VALUE_EMPTY = "School info  value empty"
    SCHOOL_INFO_GRANT_VALUE = "Enter the grant value as true or false ,cannot leave it empty"

    CHECK_CITIZEN_CATEGORY_SUCCESS ="citizen category data retrieved success"
    CHECK_CITIZEN_CATEGORY_FAILURE = "citizen category data retrieved failure"

    #get user details table

    permanent_address_does_not_exist = "permanent address does not exist in table"
    shipping_address_does_not_exist = "shipping address does not exist in table"
    address_table_query_failed = "address record for user does not exist"
    unemployed_education_details_not_present = "Unemployed details not present in table"
    employment_status_details_not_available_need_to_save = "Employment type details not available in the table need to save for user"
    employment_details_for_user_does_not_exist = "Employment details for user does not exist need to save user uuid"

    citizenship_type_not_available = "Citizen type not available"
    citizenship_record_does_not_exist = "Citizen record for user does not exist"

    enrollment_type_available_in_table = "Enrollment type not available"

    BANK_ACCOUNT_FETCHED = "Bank account list fetched successfully"
    BANK_ACCOUNT_NOT_PRESENT = "Bank accounts are not present"
    ACCOUNT_NOT_PRESENT = "Accounts is not present"
    HEADER_CONTAINS = "Something went wrong. Try again"
    DEFAULT_ACCOUNT_CANNOT_BE_DELETED = "The bank account is primary and cannot be deleted"

    BANK_ACCOUNT_REMOVED = "Bank account removed successfully"

    #bank account details

    BANK_ACCOUNT_SAVINGS="11"
    BANK_ACCOUNT_CHECKING="01"

    BANK_UUID_VALIDATION_SUCCESS = "Bank uuid validated successfully"
    BANK_UUID_VALIDATION_FAILURE = "Bank uuid validation failed"

    SUCCESS_FETCH_AVAILABLE_BALANCE = "Successfully fetched available balance"
    FAILED_FETCH_AVAILABLE_BALANCE = "Failed to get available balance"

    INVALID_REJECTION = "Invalid rejection stage"
    APPLICATION_STATUS_UPDATED = "Application status updated successfully"
    FAILED_TO_UPDATE_REJECTION = "Failed to update rejection details"
    SET_STAGE_ID_FAIL = "Selected application stage id is invalid"
    SET_STAGE_ID_NOT_ALLOWED = "You are not allowed to modify the selected stage id"
    UPDATE_STAGE_ID_FAIL = "Updating stage id by calling update-application-stage failed"
    USER_DETAILS_FAIL = "Failed to get application_uuid from onboarding/get-details API"
    STAGING_RANGE_SUCCESS = "Successfully checked stage id is present in mst_application_stage"
    STAGING_RANGE_FAIL = "Checking stage id in mst_application_stage failed"

    INVALID_APPLICATION_STATUS_ID = "Invalid application status_id"
    FAILED_UPDATE_SUCCESS_STATUS = "Failed to update application status_id"

    APPLICATION_STATUS_SUCCESS = "Application status fetched successfully"
    APPLICATION_STATUS_FAILED = "Failed to fetch application status "

    FAILED_TO_ENCRYPT_DATA = "Failed to encrypt the data"
    INVALID_INTERNAL_JWT = "Invalid internal JWT token"
    failed_toget_user_uuid_params = "Provide a valid user uuid in the params"
    APPLICATION_ID_FAIL = "User application not created"
    USER_ADRESS_SUCCESS = "successfully retrieved user info"

