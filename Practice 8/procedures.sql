CREATE OR REPLACE PROCEDURE upsert_contact(p_first VARCHAR, p_last VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE phone = p_phone) THEN
        UPDATE contacts SET first_name = p_first, last_name = p_last WHERE phone = p_phone;
        RAISE NOTICE 'Updated existing contact with phone %', p_phone;
    ELSE
        INSERT INTO contacts (first_name, last_name, phone) VALUES (p_first, p_last, p_phone);
        RAISE NOTICE 'Inserted new contact %', p_first;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_firsts TEXT[],
    p_lasts  TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i           INT;
    bad_entries TEXT := '';
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS invalid_contacts (
        first_name TEXT,
        last_name  TEXT,
        phone      TEXT,
        reason     TEXT
    ) ON COMMIT DELETE ROWS;

    FOR i IN 1 .. array_length(p_firsts, 1) LOOP
        IF p_phones[i] NOT LIKE '+%' OR length(p_phones[i]) < 10 THEN
            INSERT INTO invalid_contacts VALUES (p_firsts[i], p_lasts[i], p_phones[i], 'Invalid phone format');
        ELSE
            IF EXISTS (SELECT 1 FROM contacts WHERE phone = p_phones[i]) THEN
                UPDATE contacts
                SET first_name = p_firsts[i], last_name = p_lasts[i]
                WHERE phone = p_phones[i];
            ELSE
                INSERT INTO contacts (first_name, last_name, phone)
                VALUES (p_firsts[i], p_lasts[i], p_phones[i]);
            END IF;
        END IF;
    END LOOP;

    FOR i IN SELECT * FROM invalid_contacts LOOP
        RAISE NOTICE 'Invalid entry: % % % - %', i.first_name, i.last_name, i.phone, i.reason;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR, p_by VARCHAR DEFAULT 'name')
LANGUAGE plpgsql AS $$
BEGIN
    IF p_by = 'name' THEN
        DELETE FROM contacts WHERE first_name = p_value;
    ELSIF p_by = 'phone' THEN
        DELETE FROM contacts WHERE phone = p_value;
    ELSE
        RAISE NOTICE 'Use "name" or "phone" for p_by parameter';
    END IF;
    RAISE NOTICE 'Delete done for % = %', p_by, p_value;
END;
$$;
