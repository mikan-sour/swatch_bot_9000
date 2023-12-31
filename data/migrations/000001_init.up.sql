CREATE SCHEMA IF NOT EXISTS "sb9";

CREATE TYPE "sb9"."asset_type" AS ENUM (
  'SILHOUETTE',
  'SWATCH'
);

CREATE TABLE "sb9"."assets" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "upload_type" sb9.asset_type NOT NULL,
  "file_path" text NOT NULL,
  "created_by" int DEFAULT 1,
  "created_at" timestamp DEFAULT (now()),
  "updated_by" int DEFAULT 1,
  "updated_at" timestamp DEFAULT (now())
);

CREATE TABLE "sb9"."tags" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "tag_name" text NOT NULL,
  "created_by" int DEFAULT 1,
  "created_at" timestamp DEFAULT (now()),
  "updated_by" int DEFAULT 1,
  "updated_at" timestamp DEFAULT (now())
);

CREATE TABLE "sb9"."assets_tags" (
  "asset_id" int NOT NULL,
  "tag_id" int NOT NULL,
  "created_by" int DEFAULT 1,
  "created_at" timestamp DEFAULT (now()),
  "updated_by" int DEFAULT 1,
  "updated_at" timestamp DEFAULT (now()),
  PRIMARY KEY ("tag_id", "asset_id")
);

ALTER TABLE "sb9"."assets_tags" ADD FOREIGN KEY ("tag_id") REFERENCES "sb9"."tags" ("id") ON DELETE CASCADE ON UPDATE NO ACTION;

ALTER TABLE "sb9"."assets_tags" ADD FOREIGN KEY ("asset_id") REFERENCES "sb9"."assets" ("id") ON DELETE CASCADE ON UPDATE NO ACTION;
